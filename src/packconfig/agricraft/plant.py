"""Define the Plant class."""
from __future__ import annotations

from typing import TYPE_CHECKING

from packconfig import Range


if TYPE_CHECKING:
    from packconfig.agricraft import Mod


########################################################################################################################

class Plant(object):
    """Plant is a specific plant which can be grown in a Agricraft crop."""

    def __init__(self, mod: Mod, plant_id: str):
        """Create a new plant."""
        self.id = plant_id
        self.mod = mod

        self.growth_bonus = 0.025
        self.growth_chance = 0.9
        self.light_range = Range(10, 16)
        self.soils = ["farmland_soil"]

        self.crop_yield = None
        self.name = None
        self.parent_a = None
        self.parent_b = None
        self.path = None
        self.qualified_id = None
        self.seed_item_id = None
        self.seed_name = None
        self.seed_texture = None

    # Properties ###################################################################################

    @property
    def tier(self) -> int:
        """Get how many mutations are required before you find a plant which is native to the world."""
        parent_a_tier = 0
        if self.parent_a is not None:
            parent_a_tier = self.parent_a.tier

        parent_b_tier = 0
        if self.parent_b is not None:
            parent_b_tier = self.parent_b.tier

        return min(parent_a_tier, parent_b_tier) + 1
