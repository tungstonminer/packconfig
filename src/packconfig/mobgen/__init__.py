"""Define classes to do with entity spawning."""

from .biome_set import BiomeSet
from .loot import Loot

from .creature import Creature  # uses Loot
from .location import Location  # uses BiomeSet

from .spawn import Spawn  # uses Creature, Location

from .mob_config_file import MobConfigFile  # uses Creature, Location, Spawn
from .spawn_builder import SpawnBuilder  # uses Location, Spawn

from .experience_file import ExperienceFile  # uses MobConfigFile, Spawn
from .loot_file import LootFile  # uses Loot, MobConfigFile, Spawn
from .potential_spawn_file import PotentialSpawnFile  # uses Creature, Location, MobConfigFile, Spawn
from .spawn_file import SpawnFile  # uses Creature, Location, MobConfigFile, Spawn
from .summon_aid_file import SummonAidFile  # uses MobConfigFile, Spawn

from .config_file_set import ConfigFileSet  # uses all the *File classes

__all__ = [
    "BiomeSet",
    "ConfigFileSet",
    "Creature",
    "ExperienceFile",
    "Location",
    "Loot",
    "LootFile",
    "MobConfigFile",
    "PotentialSpawnFile",
    "Spawn",
    "SpawnBuilder",
    "SpawnFile",
    "SummonAidFile",
]
