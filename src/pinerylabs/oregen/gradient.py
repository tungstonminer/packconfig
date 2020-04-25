"""Define the Gradient class."""
from __future__ import annotations

from copy import deepcopy as deep_copy
from typing import Any, Iterable, Optional

from pinerylabs.oregen import Deposit


########################################################################################################################

class Sweep(object):
    """Sweep describes a range of values to apply to a certain property."""

    def __init__(self, name: str, start: float, finish: float):
        """Create a new sweep."""
        self.name = name
        self.start = start
        self.finish = finish
        self.percent = 0.0

    # Properties ###################################################################################

    @property
    def value(self) -> float:
        """Get the value of this sweep at a certain percent from start to finish."""
        return ((self.finish - self.start) * self.percent + self.start)

    def assign(self, target: Any, do_round: bool = True):
        """Assign the sweep's value to the named property."""
        value = round(self.value) if do_round else self.value
        setattr(target, self.name, value)

    # Public Methods ###############################################################################

    def clone(self) -> Sweep:
        """Return a copy of this object."""
        return Sweep(self.name, self.start, self.finish)


########################################################################################################################

class Gradient(object):
    """Gradient produces a JSON blob containing a set of deposits which gradually change values."""

    def __init__(self, name: str, *sweeps: Iterable[Sweep], template: Optional[Deposit] = None, step_count: int = 10):
        """Create a new Gradient."""
        self.name = name
        self.template = template
        self.sweeps = [s for s in sweeps if isinstance(s, Sweep)]
        self.step_count = step_count

    # Properties ###################################################################################

    @property
    def deposits(self) -> Iterable[Deposit]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        if self.template is None:
            raise TypeError("cannot generate JSON for a gradient without a template deposit")

        for step_index in range(0, self.step_count + 1):
            percent = step_index / self.step_count
            deposit = deep_copy(self.template)
            deposit.deposit_name += f"-{self.name}_step{step_index}"

            for sweep in self.sweeps:
                sweep.percent = percent
                if sweep.name == "center_height":
                    sweep.assign(deposit.distribution)
                elif sweep.name == "cluster_size":
                    sweep.assign(deposit)
                elif sweep.name == "max_height":
                    sweep.assign(deposit.distribution)
                elif sweep.name == "min_height":
                    sweep.assign(deposit.distribution)
                elif sweep.name == "purity":
                    sweep.assign(deposit.vein, do_round=False)
                else:
                    raise NotImplementedError(f"no known sweep of {sweep.name}")

            yield deposit

    # Public Methods ###############################################################################

    def with_template(self, template: Deposit) -> Gradient:
        """Create a new gradient using a different template deposit."""
        sweeps = [s.clone() for s in self.sweeps]
        return Gradient(self.name, *sweeps, template=template, step_count=self.step_count)
