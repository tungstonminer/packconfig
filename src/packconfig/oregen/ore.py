"""Define the Ore class."""
from __future__ import annotations

from typing import Any, Dict


########################################################################################################################

class Ore(object):
    """Ore defines a single block to be placed in the world along with the relative probability of it being selected."""

    def __init__(self, name: str, metadata: int = 0, variant: str = None, weight: int = 100):
        """Create a new ore."""
        self.name = name
        self.metadata = metadata
        self.variant = variant
        self.weight = weight

    # Properties ###################################################################################

    @property
    def short_name(self) -> str:
        """Get the short name of this ore (i.e., without the mod name)."""
        short_name = self.name
        if ":" in self.name:
            short_name = self.name[self.name.index(":")+1:]

        if self.variant is not None:
            short_name = f"{short_name}_{self.variant}"

        return short_name

    # Methods ######################################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this ore suitable for being converted to JSON."""
        if self.metadata == 0 and self.variant is None and self.weight == 100:
            return self.name
        else:
            result = {"name": self.name}

            if self.metadata != 0:
                result["metadata"] = self.metadata
            if self.variant is not None:
                result["properties"] = {"variant": self.variant}
            if self.weight != 100:
                result["weight"] = self.weight

            return result

    def weighted(self, weight) -> Ore:
        """Create a new ore from this one with a different weighting."""
        return Ore(self.name, self.metadata, self.variant, weight)

    # Overridden Methods ###########################################################################

    def __repr__(self) -> str:
        """Get a string representation of this object."""
        if self.variant is not None:
            return f"Ore<name: {self.name}, variant: {self.variant}, weight: {self.weight}>"
        elif self.metadata != 0:
            return f"Ore<name: {self.name}, metadata: {self.metadata}, weight: {self.weight}>"
        else:
            return f"Ore<name: {self.name}, weight: {self.weight}>"
