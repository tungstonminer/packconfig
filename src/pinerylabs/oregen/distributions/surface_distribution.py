"""Define the SurfaceDistribution class."""

from typing import Any, Dict

from pinerylabs.oregen import Distribution


########################################################################################################################

class SurfaceDistribution(Distribution):
    """SurfaceDistribution places deposits on the surface of the world."""

    def __init__(self, name: str, follow_terrain: bool = True):
        """Create a new uniform distribution."""
        super().__init__(name)
        self.follow_terrain = follow_terrain

    # Overridden Methods ###########################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        return {
            "distribution": "surface",
            # COFH World has a bug where follow-terrain is inverted, so we flip the value here.
            "follow-terrain": not self.follow_terrain,
        }
