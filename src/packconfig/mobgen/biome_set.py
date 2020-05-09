"""Define the BiomeSet class."""
from __future__ import annotations

from typing import Iterable

from packconfig.oregen import OreList, OreListable
from packconfig.oregen.data import vanilla as mc


########################################################################################################################

all_names = set()


########################################################################################################################

class BiomeSet(object):
    """BiomeSet describes a group of biomes suitable for mob placement along with their normal block types."""

    ANY = None

    def __init__(self, *names: Iterable[str], blocks: OreListable = None, underground: bool = False):
        """Create a new biome set."""
        self._names = set()

        self.blocks = OreList.convert(blocks)
        self.underground = underground

        for name in names:
            self.add_biome(name)

        if self.blocks is None:
            if self.underground:
                self.blocks = OreList(mc.stone)
            else:
                self.blocks = OreList(mc.grass, mc.dirt, mc.sand)

        if BiomeSet.ANY is None:
            BiomeSet.ANY = ""
            BiomeSet.ANY = BiomeSet(None)

    # Class Methods ################################################################################

    @staticmethod
    def merge(*biome_sets: Iterable[BiomeSet], blocks: OreListable = None):
        """Merge several biome sets together."""
        result = BiomeSet(None, blocks=blocks)
        for biome_set in biome_sets:
            for name in biome_set.names:
                result.add_biome(name)

        return result

    # Properties ###################################################################################

    @property
    def names(self) -> Iterable[str]:
        """List the names of all the biomes in this set."""
        if self is BiomeSet.ANY:
            global all_names
            for name in sorted(all_names):
                yield name

        for name in sorted(self._names):
            yield name

    # Public Methods ###############################################################################

    def add_biome(self, name: str) -> BiomeSet:
        """Add a biome to this set."""
        if name is None:
            return

        global all_names
        all_names.add(name)

        self._names.add(name)
        return self

    def with_blocks(self, *blocks: OreListable):
        """Create a new BiomeSet using a different set of surfaces blocks."""
        return BiomeSet(*self.names, blocks=blocks, underground=self.underground)

    def in_cave(self):
        """Create a new BiomeSet specifying the caves in the current set of biomes."""
        return BiomeSet(*self.names, blocks=None, underground=True)

    def in_sky(self):
        """Create a new BiomeSet specifying the air above the current set of biomes."""
        return BiomeSet(*self.names, blocks=mc.air, underground=self.underground)

    def in_water(self):
        """Create a new BiomeSet specifying any pools or lakes in the current set of biomes."""
        return BiomeSet(*self.names, blocks=mc.water, underground=self.underground)
