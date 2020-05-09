"""Define the Range class."""
from __future__ import annotations

from collections import namedtuple
from typing import Iterable, Optional


########################################################################################################################

class Range(object):
    """Range represents a value which has an upper and lower bound."""

    def __init__(self, lower: Optional[int], upper: Optional[int]):
        """Define a new range."""
        self._lower = lower
        self._upper = upper

    # Class Methods ################################################################################

    def invert(self, bounds: Range, *ranges: Iterable[Range]):
        """Create a set of ranges which covers the inverse of the given bounds."""
        Boundary = namedtuple("Boundary", "value kind")
        boundaries = []
        boundaries.extend(Boundary(r.lower, "start") for r in ranges)
        boundaries.extend(Boundary(r.upper, "end") for r in ranges)
        boundaries.sort(key=lambda b: b.value)

        result = []
        current_start = bounds.start
        depth = 0
        for boundary in boundaries:
            depth += 1 if boundary.kind == "start" else -1

            if depth == 1:
                result.append(Range(current_start, boundary.value))
                current_start = None
            elif depth == 0:
                current_start = boundary.value

        if current_start is not None:
            result.append(Range(current_start, bounds.upper))

        return result

    # Properties ###################################################################################

    @property
    def lower(self) -> Optional[int]:
        """Get the lower bound of this range."""
        return self._lower

    @property
    def upper(self) -> Optional[int]:
        """Get the upper bound of this range."""
        return self._upper

    # Public Methods ###############################################################################

    def clone(self):
        """Create an exact copy of this range."""
        return Range(self.lower, self.upper)

    # Magic Methods ################################################################################

    def __repr__(self) -> str:
        """Get a string representation of this range."""
        return f"{self.lower}:{self.upper}"
