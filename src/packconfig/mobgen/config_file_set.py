"""Define the ConfigFileSet class."""

from typing import Iterable, Optional

from packconfig.mobgen import ExperienceFile, LootFile, PotentialSpawnFile, Spawn, SpawnFile, SummonAidFile


########################################################################################################################

class ConfigFileSet(object):
    """ConfigFileSet pulls together all the config files needed to fully specify mob spawning for the game."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new config file set."""
        self.config_files = [
            ExperienceFile(*spawns),
            LootFile(*spawns),
            PotentialSpawnFile(*spawns),
            SpawnFile(*spawns),
            SummonAidFile(*spawns),
        ]

    # Public Methods ###############################################################################

    def generate(self, target_dir: Optional[str]):
        """Generate the config files into the target directory."""
        for config_file in self.config_files:
            config_file.write(target_dir)
