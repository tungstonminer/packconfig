"""Define the ConfigFile class."""
from __future__ import annotations

import json
import os

from contextlib import contextmanager
from io import FileIO
from typing import Any, Dict, Iterable, Union

from pinerylabs.oregen import BiomeSet, Deposit, Distribution, Gradient


########################################################################################################################

class ConfigFile(object):
    """ConfigFile represents a single config file for COFHWorld."""

    def __init__(self, file_name: str, enabled: bool = True, priority: int = 100):
        """Create a new config file."""
        self.enabled = enabled
        self.file_name = file_name
        self.priority = priority

        self._biomes_override = None
        self._distribution_override = None
        self._deposits = []
        self._dimension_override = None

    # Properties ###################################################################################

    @property
    def deposits(self) -> Iterable[Deposit]:
        """Iterate over all the deposits in this config file."""
        for deposit in self._deposits:
            yield deposit

    # Public Methods ###############################################################################

    def add(self, arg: Union[Gradient, Deposit]) -> ConfigFile:
        """Add a deposit to this config file."""
        if isinstance(arg, Deposit):
            deposits = [arg]
        elif isinstance(arg, Gradient):
            deposits = list(arg.deposits)
        else:
            raise TypeError(f"can only add a Deposit or Gradient, not a {type(arg).__name__}")

        for deposit in deposits:
            if self._biomes_override is not None:
                deposit.biomes = self._biomes_override
            if self._distribution_override is not None:
                deposit.distribution = self._distribution_override
            if self._dimension_override is not None:
                deposit.dimension = self._dimension_override

            self._deposits.append(deposit)

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        return {
            "enabled": self.enabled,
            "priority": self.priority,
            "populate": {d.name.lower(): d.as_json() for d in self.deposits}
        }

    def print(self):
        """Print the JSON text of this file to stdout."""
        print(json.dumps(self.as_json(), indent="    "))

    def write_file(self, target_dir: str):
        """Write the contents of this config file to disk in the indicated directory."""
        with FileIO(os.path.join(target_dir, self.file_name), "w") as f:
            text = json.dumps(self.as_json(), indent="    ")
            f.write(text.encode("utf-8"))

    # Context Managers #############################################################################

    @contextmanager
    def distribution(self, distribution: Distribution) -> ConfigFile:
        """Override the biome of any enclosed deposit."""
        try:
            self._distribution_override = distribution
            yield self
        finally:
            self._distribution_override = None

    @contextmanager
    def biomes(self, biomes: BiomeSet) -> ConfigFile:
        """Override the biome of any enclosed deposit."""
        try:
            self._biomes_override = biomes
            yield self
        finally:
            self._biomes_override = None

    @contextmanager
    def dimension(self, dimension: int) -> ConfigFile:
        """Override the biome of any enclosed deposit."""
        try:
            self._dimension_override = dimension
            yield self
        finally:
            self._dimension_override = None

    # Magic Methods ################################################################################

    def __enter__(self) -> ConfigFile:
        """Begin a context with this file."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Exit the context using this file."""
        return False
