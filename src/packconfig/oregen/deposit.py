"""Define the Deposit class."""

import hashlib

from typing import Any, Dict

from packconfig.oregen import BiomeSet, Distribution, OreList, OreListable, Vein
from packconfig.oregen.distributions import UniformDistribution


########################################################################################################################

class Deposit(object):
    """
    Deposit represents the placement of a vein in the world.

    This class is inteded to be subclassed by various specific kinds of deposits (e.g., cluster, plate, lake, etc.).
    If used directly, this class won't actually place any ore in the world.
    """

    def __init__(
        self,
        vein: Vein,
        deposit_name: str = None,
        biomes: BiomeSet = None,
        cluster_count: int = 1,
        distribution: Distribution = None,
        replaces: OreListable = None,
        percent: int = 100,
        dimension: int = 0,
    ):
        """Create a new deposit."""
        self.biomes = biomes if biomes is not None else BiomeSet.ANY
        self.base_cluster_count = cluster_count
        self.deposit_name = deposit_name if deposit_name is not None else vein.name
        self.dimension = dimension
        self.distribution = distribution if distribution is not None else UniformDistribution("any", 0, 256)
        self.percent = percent
        self.replaces = OreList.convert(replaces if replaces is not None else vein.material_ore)
        self.vein = vein

    # Properties ###################################################################################

    @property
    def biomes(self) -> BiomeSet:
        """Get the set of biomes in which this deposit may appear."""
        return self._biomes

    @biomes.setter
    def biomes(self, value: BiomeSet):
        self._biomes = value
        self._compute_id()

    @property
    def chunk_chance(self):
        """Get the liklihood this deposit will form in a given chunk expressed as: 1 / chunk_chance."""
        return max(1, round(100.0 / self.percent))

    @property
    def cluster_count(self):
        """Get the number of attempts made to place this deposit in a given chunk."""
        return self.distribution.scale_cluster_count(self.base_cluster_count)

    @property
    def name(self):
        """Get the name of this deposit in the config file."""
        return f"{self.deposit_name.upper()}-{self.distribution.name}-{self.id}"

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = {
            "chunk-chance": self.chunk_chance,
            "cluster-count": self.cluster_count,
            "biome": self.biomes.as_json(),
            "generator": {
                "block": self.vein.as_json(),
            },
        }

        if self.dimension == 0:
            # Assume overworld settings are for *any* worlds
            result.update({
                "dimension": {
                    "restriction": "blacklist",
                    "value": [-1, 1],
                }
            })
        else:
            result.update({
                "dimension": {
                    "restriction": "whitelist",
                    "value": [self.dimension],
                }
            })

        if self.replaces is not None:
            result["generator"].update({
                "material": self.replaces.as_json()
            })

        result.update(self.distribution.as_json())

        return result

    # Private Methods ##############################################################################

    def _compute_id(self):
        hasher = hashlib.new("md5")
        for biome in self.biomes.biomes:
            hasher.update(biome.encode("UTF-8"))
        self.id = hasher.hexdigest()
