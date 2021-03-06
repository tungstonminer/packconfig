"""Define various kinds of deposits."""

from .boulder_deposit import BoulderDeposit
from .cave_deposit import CaveDeposit
from .cluster_deposit import ClusterDeposit
from .geode_deposit import GeodeDeposit
from .lake_deposit import LakeDeposit
from .plate_deposit import PlateDeposit

__all__ = [
    "BoulderDeposit",
    "CaveDeposit",
    "ClusterDeposit",
    "GeodeDeposit",
    "LakeDeposit",
    "PlateDeposit",
]
