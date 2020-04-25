"""Define the NormalDistribution class."""

from typing import Any, Dict

from pinerylabs.oregen import Distribution


########################################################################################################################

class NormalDistribution(Distribution):
    """NormalDistribution places deposits in a normal distribution around a central point."""

    def __init__(self, name: str, center_height: int, spread: int = 16, smoothness: int = 2):
        """Create a new uniform distribution."""
        super().__init__(name)
        self.center_height = center_height
        self.spread = spread
        self.smoothness = smoothness

    # Properties ###################################################################################

    @property
    def total_height(self) -> int:
        """Get the total height of between the ceiling and floor of this distribution."""
        return self.spread * 2

    # Overridden Methods ###########################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        return {
            "distribution": "gaussian",
            "center-height": self.center_height,
            "spread": self.spread,
            "smoothness": self.smoothness,
        }

    def scale_cluster_count(self, cluster_count: int) -> int:
        """Scale the cluster count to maintain roughly `cluster_count` occurances per 16m cube."""
        return max(1, round(self.total_height / 16.0 * cluster_count / 2.0))
