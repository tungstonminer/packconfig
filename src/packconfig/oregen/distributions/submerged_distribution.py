"""Define the SubmergedDistribution class."""

from typing import Any, Dict

from packconfig.oregen import Distribution, OreList, OreListable


########################################################################################################################

class SubmergedDistribution(Distribution):
    """SubmergedDistribution places deposits immediately below a body of liquid.."""

    def __init__(self, name: str, fluid: OreListable, material: OreListable = None):
        """Create a new uniform distribution."""
        super().__init__(name)
        self.fluid = OreList(fluid)
        self.material = OreList(material)

    # Overridden Methods ###########################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this deposit suitable for being converted to JSON."""
        result = {
            "distribution": "underfluid",
            "fluid": self.fluid.as_json(),
        }
        if not self.material.is_empty:
            result["material"] = self.material.as_json()

        return result
