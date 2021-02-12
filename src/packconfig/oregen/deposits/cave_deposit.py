"""Define the CaveDeposit class."""

from packconfig.oregen import Deposit, Vein


########################################################################################################################

class CaveDeposit(Deposit):
    """CaveDeposit create s a deposit as a stalagtite/mite on a cave wall."""

    def __init__(self, vein: Vein, ceiling: bool = True, cluster_size: int = 8, cluster_count: int = 1, **kwargs):
        """
        Create a new cave deposit.

        Arguments:
            vein: a Vein describing what block(s) are to be replaced with which other blocks
            cluster_size: how many blocks (approximately) should each cluster contain

        """
        super().__init__(vein, **kwargs)

        self.ceiling = ceiling
        self.cluster_size = cluster_size
        self._cluster_count = cluster_count

    # Properties ###################################################################################

    @property
    def cluster_count(self):
        """Get the number of attempts made to place this deposit in a given chunk."""
        return self._cluster_count

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["distribution"] = "cave"
        result["ceiling"] = "true" if self.ceiling else "false"
        result["generator"].update({
            "block": self.vein.with_purity(100).as_json(),
            "cluster-size": self.cluster_size,
            "type": "cluster",
        })
        return result
