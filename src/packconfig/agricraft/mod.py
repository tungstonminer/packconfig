"""Define the Mod class."""

import inflection

from packconfig import Range
from packconfig.agricraft import CropYield, Plant


########################################################################################################################

class Mod(object):
    """Mod represents a Minecraft mod which adds growable plants."""

    def __init__(self, mod_id: str):
        """Create a new mod."""
        self.mod_id = mod_id
        self.plants = []

    # Public Methods ###############################################################################

    def create_plant(self, plant_id: str, plant_name: str):
        """Create a new plant which belongs to this mod."""
        plant = Plant(self, plant_id)
        plant.path = self.get_plant_path(plant_id)
        plant.name = plant_name
        plant.seed_name = self.get_plant_seed_item_name(plant_name)
        plant.seed_item_id = self.get_plant_seed_item(plant_id)
        plant.qualified_id = self.get_qualified_id(plant_id)
        plant.crop_yield = [CropYield(self.get_crop_id(plant_id), Range(1, 4), 0.80)]
        plant.seed_texture = self.get_seed_texture(plant_id)

        self.plants.append(plant)
        plant.mod = self
        return plant

    def get_crop_id(self, plant_id: str) -> str:
        """Get the Minecraft id of the crop item grown by this plant."""
        return f"{self.id}:{plant_id}item"

    def get_plant_name(self, plant_id: str) -> str:
        """Get the human-readable name of this plant."""
        return inflection.titleize(plant_id)

    def get_plant_path(self, plant_id: str) -> str:
        """Get the path where this plant's config file may be found."""
        return f"mod_{self.mod_id}/plants/{plant_id}_plant.json"

    def get_plant_seed_item_id(self, plant_id: str) -> str:
        """Get the Minecraft id of the seed item for this plant."""
        return f"{self.mod_id}:{plant_id}seeditem"

    def get_plant_seed_item_name(self, plant_name: str) -> str:
        """Get the human-readable name for the seed which produces the given plant."""
        return f"{plant_name} Seed"

    def get_qualified_id(self, plant_id: str) -> str:
        """Get the fully-qualified identifier for the given plant."""
        return f"{self.id}:{plant_id}"

    def get_seed_texture(self, plant_id: str) -> str:
        """Get the location of the image providing the texture of this plant's seed."""
        return f"{self.id}:items/{plant_id}seeditem"
