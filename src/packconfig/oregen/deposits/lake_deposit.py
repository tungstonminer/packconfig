"""Define the LakeDeposit class."""

from packconfig.oregen import Deposit, OreList, OreListable, Vein


########################################################################################################################

class LakeDeposit(Deposit):
    """LakeDeposit creates a deposit as a shell around a small pond of some fluid."""

    def __init__(self, vein: Vein, liquid: OreListable, diameter: int = 8, **kwargs):
        """Create a new lake deposit."""
        liquid = OreList.convert(liquid)
        if "deposit_name" not in kwargs:
            kwargs["deposit_name"] = f"{liquid.short_name}-{vein.name}-LAKE"
        super().__init__(vein, **kwargs)

        self.diameter = diameter
        self.liquid = liquid

    def as_json(self):
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = super().as_json()
        result["generator"].update({
            "block": self.liquid.as_json(),
            "cluster-size": self.diameter,
            "outline-block": self.vein.as_json(),
            "solid-outline": True,
            "type": "lake",
            "use-material": True,
        })

        return result
