"""Define the UniformDistribution class."""

from typing import Any, Dict

from packconfig.oregen import Distribution


########################################################################################################################

class UniformDistribution(Distribution):
    """UniformDistribution distributes deposits uniformly within a range of altitudes."""

    def __init__(self, name: str, min_height: int, max_height: int):
        """Create a new uniform distribution."""
        super().__init__(name)
        self.min_height = min_height
        self.max_height = max_height

    # Properties ###################################################################################

    @property
    def total_height(self) -> int:
        """Get the total height of between the ceiling and floor of this distribution."""
        return self.max_height - self.min_height

    # Overridden Methods ###########################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        return {
            "distribution": "uniform",
            "min-height": self.min_height,
            "max-height": self.max_height,
        }

    def scale_cluster_count(self, cluster_count: int) -> int:
        """Scale the cluster count to maintain roughly `cluster_count` occurances per 16m cube."""
        return max(1, round(self.total_height / 16.0 * cluster_count))
