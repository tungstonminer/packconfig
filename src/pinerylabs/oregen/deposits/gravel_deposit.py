"""Define the GravelDeposit class."""

from pinerylabs.oregen import Deposit, Vein


########################################################################################################################

class GravelDeposit(Deposit):
    """GravelDeposit create s a deposit as a large cylinder of the given material."""

    def __init__(self, vein: Vein, height: int = 2, diameter: int = 16, **kwargs):
        """Create a new plate deposit."""
        if "deposit_name" not in kwargs:
            kwargs["deposit_name"] = vein.name
        if "material" not in kwargs:
            kwargs["material"] = vein.material_ore

        super().__init__(**kwargs)

        self.diameter = diameter
        self.height = height
        self.vein = vein

    # Methods ######################################################################################

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "block": self.vein.as_json(),
            "height": max(0, round(self.height / 2.0)),
            "radius": max(1, round(self.diameter / 2.0)),
            "slim": (self.height % 2) == 1,
            "type": "plate",
        })
        return result
