"""Define the GeodeDeposit class."""

from pinerylabs.oregen import Deposit, Vein


########################################################################################################################

class GeodeDeposit(Deposit):
    """GeodeDeposit creates a single (potentially hollow) geode."""

    def __init__(self, crust: Vein, filler: Vein = None, **kwargs):
        """
        Create a new geode deposit.

        Arguments:
            crust: a Vein describing the outer shell of the geode
            filler: a Vein describing the inside of the geode. If not provided, the geode will be solid crust.
            kwargs: all the arguments permitted by Deposit

        """
        super().__init__(crust, **kwargs)

        self.filler = filler

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "crust": self.vein.as_json(),
            "type": "geode",
        })
        if self.filler:
            result["generator"].update({
                "hollow": True,
                "filler": self.filler.as_json(),
            })

        return result
