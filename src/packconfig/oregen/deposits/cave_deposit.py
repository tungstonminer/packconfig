"""Define the CaveDeposit class."""

from typing import Optional

from packconfig.oregen import Deposit, Vein


########################################################################################################################

class CaveDeposit(Deposit):
    """CaveDeposit create s a deposit as a stalagtite/mite on a cave wall."""

    def __init__(
        self,
        vein: Vein,
        ceiling: bool = True,
        cluster_size: int = 8,
        cluster_count: int = 1,
        max_elevation: Optional[int] = None,
        **kwargs
    ):
        """
        Create a new cave deposit.

        Arguments:
            vein: a Vein describing what block(s) are to be replaced with which other blocks
            cluster_size: how many blocks (approximately) should each cluster contain
            max_elevation: the maximum elevation at which the deposit should appear

        """
        super().__init__(vein, **kwargs)

        self.ceiling = ceiling
        self.cluster_size = cluster_size
        self.max_elevation = max_elevation
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
        if self.max_elevation is not None:
            result["ground-level"] = self.max_elevation

        return result
