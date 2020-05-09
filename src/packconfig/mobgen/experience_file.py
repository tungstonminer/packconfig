"""Define the ExperienceFile class."""

from typing import Iterable

from packconfig.mobgen import MobConfigFile, Spawn


########################################################################################################################

class ExperienceFile(MobConfigFile):
    """ExperienceFile defines how much experience you get from killing mobs."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new config file."""
        super().__init__("experience.json", *spawns)
