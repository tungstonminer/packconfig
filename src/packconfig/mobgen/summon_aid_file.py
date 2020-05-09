"""Define the SummonAidFile class."""

from typing import Iterable

from packconfig.mobgen import MobConfigFile, Spawn


########################################################################################################################

class SummonAidFile(MobConfigFile):
    """SummonAidFile species rules for how mobs may summon the aid of other mobs."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new config file."""
        super().__init__("summonaid.json", *spawns)
