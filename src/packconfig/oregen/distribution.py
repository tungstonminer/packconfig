"""Define the Distribution class."""

from typing import Any, Dict


########################################################################################################################

class Distribution(object):
    """Distribution describes where a deposit is placed in the world."""

    def __init__(self, name: str):
        """Create a new distribution."""
        self.name = name

    # Public Methods ###############################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        raise NotImplementedError(f"{type(self).__name__} must override `as_json`")

    def scale_cluster_count(self, cluster_count: int) -> int:
        """Scale the cluster count to maintain roughly `cluster_count` occurances per 16m cube."""
        return cluster_count
