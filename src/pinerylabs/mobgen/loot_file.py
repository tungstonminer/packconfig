"""Define the LootFile class."""

from typing import Iterable

from pinerylabs.mobgen import MobConfigFile, Spawn


########################################################################################################################

class LootFile(MobConfigFile):
    """LootFile defines what loot you get from killing certain creatures."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new config file."""
        super().__init__("loot.json", *spawns)
