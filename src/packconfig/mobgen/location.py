"""Define the Location class."""

from typing import Optional

from packconfig.mobgen import BiomeSet, Range


########################################################################################################################

class Location(object):
    """Location describes the physical space in which a spawn may happen."""

    def __init__(
        self,
        biomes: BiomeSet,
        altitude: Range = None,
        dimension: Optional[int] = None,
        structure: str = None,
        weather: str = None,
    ):
        """Create a new spawn location."""
        self.altitude = altitude
        self.biomes = biomes
        self.dimension = dimension
        self.structure = structure
        self.weather = weather

        if self.altitude is None:
            self.altitude = Range(0, 256)
