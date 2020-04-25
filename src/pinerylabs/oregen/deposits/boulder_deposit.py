"""Define the BoulderDeposit class."""

from pinerylabs.oregen import Deposit, Quantity, Quantityable, Vein


########################################################################################################################

class BoulderDeposit(Deposit):
    """BoulderDeposit creates a cluster of boulders of a given vein."""

    def __init__(
        self,
        vein: Vein,
        diameter: Quantityable = 1,
        count: Quantityable = 1,
        hollow_size: Quantityable = None,
        **kwargs,
    ):
        """
        Create a new cluster deposit.

        Arguments:
            vein: a Vein describing what block(s) should make up the boulder
            diameter: the diameter of each individual boulder in the group
            count: the number of boulders in the group
            hollow_size: how large is the hollow portion of the boulder
            kwargs: all the arguments permitted by Deposit

        """
        super().__init__(vein, **kwargs)

        self.count = Quantity.convert(count)
        self.diameter = Quantity.convert(diameter)
        self.hollow_size = Quantity.convert(hollow_size)

        # allow "None" as a replaces value
        if "replaces" in kwargs:
            self.replaces = kwargs["replaces"]
        else:
            self.replaces = None

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "block": self.vein.as_json(),
            "count": self.count.minimum,
            "count-variance": self.count.variance,
            "diameter": max(1, round(self.diameter.minimum / 2.0)),
            "size-variance": round(self.diameter.variance / 2.0),
            "type": "boulder",
        })
        if self.hollow_size is not None:
            result["generator"].update({
                "hollow": True,
                "hollow-size": self.hollow_size.minimum,
                "hollow-variance": self.hollow_size.variance,
            })

        return result
