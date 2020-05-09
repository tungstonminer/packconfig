"""Define the Vein class."""
from __future__ import annotations

from typing import Any, Dict, Iterable, Optional

from packconfig.oregen import Ore, OreList


########################################################################################################################

class Vein(object):
    """Vein represents a mixutre of ores in some base material."""

    def __init__(
        self,
        *ores: Iterable[Ore],
        material_ore: Optional[Ore] = None,
        name: Optional[str] = None,
        purity: int = 100,
    ):
        """
        Create a new vein with a certain name, base material, and collection of ores.

        Arguments:
            ores: an iterable collection of Ores to include in this vein
            material_ore: a single Ore used as filler for veins of less than 100% purity
            name: an alternate name to use in case the name of the first ore isn't desired
            purity: a value between 0–100 giving the percentage of the vein made of ore

        """
        self.ores = OreList.convert(ores)

        self.name = name if name is not None else self.ores.short_name
        self.material_ore = material_ore if material_ore is not None else Ore("minecraft:stone", 0)
        self.purity = purity

    # Methods ######################################################################################

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this vein suitable for being converted to JSON."""
        results = []
        if self.purity != 100:
            results.append(self.material_ore.weighted(round(1000.0 * (100 - self.purity))))

        for ore in self.ores.ores:
            weight = round(1000.0 * ore.weight * self.purity / 100)
            if weight >= 1:
                results.append(ore.weighted(weight))

        if len(results) == 1:
            return results[0].weighted(100).as_json()

        return [o.as_json() for o in results]

    def with_purity(self, purity) -> Vein:
        """Create a new vein with an indicated percentage of ores vs base material."""
        return Vein(*self.ores.ores, material_ore=self.material_ore, name=self.name, purity=purity)

    # Overridden Methods ###########################################################################

    def __repr__(self) -> str:
        """Get a string representation of this object."""
        ores_text = ", ".join(str(o) for o in self.ores)
        return f"Vein<name: {self.name}, material_ore: {self.material_ore}, purity: {self.purity}, ores: {ores_text}>"
