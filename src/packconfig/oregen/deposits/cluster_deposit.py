"""Define the ClusterDeposit class."""

from packconfig.oregen import Deposit, Vein


########################################################################################################################

class ClusterDeposit(Deposit):
    """ClusterDeposit create s a deposit as a large cylinder of the given material."""

    def __init__(self, vein: Vein, cluster_size: int = 8, **kwargs):
        """
        Create a new cluster deposit.

        Arguments:
            vein: a Vein describing what block(s) are to be replaced with which other blocks
            cluster_size: how many blocks (approximately) should each cluster contain

        """
        super().__init__(vein, **kwargs)

        self.cluster_size = cluster_size

    # Properties ###################################################################################

    @property
    def cluster_count(self) -> int:
        """
        Get how many clusters should be generated.

        This uses the purity property of the vein to figure out how many clusters would be needed to create an overall
        percent of ore in the region described by this deposit. This will be something of an approximation since the
        cluster sizes are somewhat approximate, but it will be pretty close.
        """
        cluster_count = max(1, round(16**3 * (self.vein.purity / 100.0) / self.cluster_size))
        return self.distribution.scale_cluster_count(cluster_count)

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "block": self.vein.with_purity(100).as_json(),
            "cluster-size": self.cluster_size,
            "type": "cluster",
        })
        return result
