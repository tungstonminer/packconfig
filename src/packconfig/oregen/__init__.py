"""Define the oregen module."""

from .biome_set import BiomeSet
from .distribution import Distribution
from .ore import Ore
from .quantity import Quantity, Quantityable

from .ore_list import OreList, OreListable  # uses Ore
from .vein import Vein  # uses Ore

from .asteroid import Asteroid  # uses Ore, Quantity, Vein
from .deposit import Deposit  # uses BiomeSet, OreList, Vein

from .asteroid_file import AsteroidFile  # uses Asteroid
from .gradient import Gradient, Sweep  # uses Deposit

from .config_file import ConfigFile  # uses Deposit, Gradient

__all__ = [
    "Asteroid",
    "AsteroidFile",
    "BiomeSet",
    "ConfigFile",
    "Deposit",
    "Distribution",
    "Endpoint",
    "Gradient",
    "Ore",
    "OreList",
    "OreListable",
    "Quantity",
    "Quantityable",
    "Sweep",
    "Vein",
]
