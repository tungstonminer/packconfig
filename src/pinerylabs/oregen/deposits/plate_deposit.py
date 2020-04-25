"""Define the PlateDeposit class."""

from pinerylabs.oregen import Deposit, Vein


########################################################################################################################

class PlateDeposit(Deposit):
    """PlateDeposit create s a deposit as a large cylinder of the given material."""

    def __init__(self, vein: Vein, height: int = 2, diameter: int = 16, is_round: bool = True, **kwargs):
        """Create a new plate deposit."""
        super().__init__(vein, **kwargs)
        self.diameter = diameter
        self.height = height
        self.is_round = is_round

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "height": max(0, round(self.height / 2.0)),
            "radius": max(1, round(self.diameter / 2.0)),
            "shape": "CIRCLE" if self.is_round else "SQUARE",
            "slim": (self.height % 2) == 1,
            "type": "plate",
        })

        return result
