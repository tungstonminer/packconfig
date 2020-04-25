"""Define the BiomeSet class."""
from __future__ import annotations

from typing import Any, Dict, Iterable, Union


########################################################################################################################

ALL_BIOMES = None


########################################################################################################################

class BiomeSet(object):
    """BiomeSet represents a grouping of biomes sharing some common trait."""

    ANY = None

    def __init__(self, *biomes: Iterable[str]):
        """Create a new set of biomes."""
        global ALL_BIOMES
        if ALL_BIOMES is None:
            ALL_BIOMES = ""  # avoid recursion
            ALL_BIOMES = BiomeSet()

        if BiomeSet.ANY is None:
            BiomeSet.ANY = ""
            BiomeSet.ANY = BiomeSet()

        self._biomes = set()
        if len(biomes) > 0:
            self.include(*biomes)
            ALL_BIOMES.add(self)

    # Class Methods ################################################################################

    @staticmethod
    def all_biomes() -> BiomeSet:
        """Create a new biome set as the union of all known biomes."""
        global ALL_BIOMES
        return BiomeSet().add(ALL_BIOMES)

    # Properties ###################################################################################

    @property
    def biomes(self) -> Iterable[str]:
        """Get an iterable list of biomes in this set."""
        for biome in self._biomes:
            yield biome

    # Methods ######################################################################################

    def add(self, *otherSets: Iterable[BiomeSet]) -> BiomeSet:
        """Update this biome set to include all the biomes in several other sets."""
        for otherSet in otherSets:
            self._biomes.update(otherSet.biomes)
        return self

    def as_json(self) -> Union[str, Dict[str, Any]]:
        """Create a dict representation of this biome set suitable for being converted to JSON."""
        if self is BiomeSet.ANY:
            return "any"

        return {
            "restriction": "whitelist",
            "value": [{
                "type": "id",
                "entry": sorted(self.biomes),
            }]
        }

    def include(self, *biomes: Iterable[BiomeSet]) -> BiomeSet:
        """Include more biomes in this set."""
        for biome in biomes:
            self._biomes.add(biome)

    def remove(self, *otherSets: Iterable[BiomeSet]) -> BiomeSet:
        """Update this biome set to remove all the biomes included in several other sets."""
        for otherSet in otherSets:
            self._biomes.difference_update(otherSet.biomes)
        return self

    def intersect(self, *otherSets: Iterable[BiomeSet]) -> BiomeSet:
        """Update this biome set to include only those biomes in this and several other sets."""
        for otherSet in otherSets:
            self._biomes.intersection_update(otherSet.biomes)
        return self

    # Overridden Methods ###########################################################################

    def __repr__(self) -> str:
        """Provide a string representation of this biome set."""
        return f"BiomeSet<{', '.join(b for b in self.biomes)}>"
