"""Define the Creature class."""
from __future__ import annotations

from typing import Iterable, Optional

from pinerylabs.mobgen import Range


########################################################################################################################

class Creature(object):
    """Creature defines the placement of a cluster of a single kind of creature."""

    def __init__(
        self,
        entity_id: str,
        group_size: Range = None,
        active_periods: Iterable[Range] = None,
        rarity: int = 1,
        groups_allowed: int = 1,
    ):
        """
        Define a new creature group.

        Arguments:
            entity_id: a str containing the in-game id of the entity (e.g., "minecraft:cow")
            group_size: a Range giving how many entities may appear in a single group
            active_periods: a list of Ranges giving the times of day when this creature is active (0=dawn, 12000=sunset)
            rarity: the chances out of 1000 that this creature will be select spawn on any tick. If the sum of rarity
                scores in a single spawn point exceeds 1000, the relative rarity of each creature will be weighed
                against the others when choosing the next group to spawn each tick
            groups_allowed: the number of filled groups which should be permitted to spawn at once
        """
        self.active_periods = active_periods
        self.entity_id = entity_id
        self.group_size = group_size
        self.rarity = rarity
        self.groups_allowed = groups_allowed

        if self.active_periods is None:
            self.active_periods = [Range(0, 24000)]

        self.active_periods = [r.clone() for r in self.active_periods]

        if self.group_size is None:
            self.group_size = Range(1, 1)

        self.group_size = self.group_size.clone()

    # Properties ###################################################################################

    @property
    def is_always_active(self) -> bool:
        """Return whether this creature is active at all times of day."""
        if len(self.active_periods) == 0:
            return True

        if len(self.active_periods) == 1:
            period = self.active_periods[0]
            if period.lower == 0 and period.upper == 24000:
                return True

        return False

    @property
    def max_individuals(self) -> int:
        """Get the maximum number of individuals which should be permitted based upon group size and count."""
        return self.group_size.upper * self.groups_allowed

    # Public Methods ###############################################################################

    def configure(
        self,
        rarity: Optional[int] = None,
        groups_allowed: Optional[int] = None,
        group_size: Optional[Range] = None,
    ):
        """Create a copy of this creature with a set of changes."""
        group_size = group_size if group_size is not None else self.group_size
        groups_allowed = groups_allowed if groups_allowed is not None else self.groups_allowed
        rarity = rarity if rarity is not None else self.rarity

        return Creature(self.entity_id, group_size, self.active_periods, rarity, groups_allowed)

    def with_active_periods(self, *active_periods: Iterable[Range]) -> Creature:
        """Create a new creature with a different set of activity periods."""
        return Creature(self.entity_id, self.group_size, active_periods, self.rarity, self.groups_allowed)

    def with_group_size(self, lower: int, upper: int) -> Creature:
        """Return a new Creature with a different group size."""
        return Creature(self.entity_id, Range(lower, upper), self.active_periods, self.rarity, self.groups_allowed)

    def with_groups_allowed(self, groups_allowed: int) -> Creature:
        """Return a new creature with a different number of groups allowed."""
        return Creature(self.entity_id, self.group_size, self.active_periods, self.rarity, groups_allowed)

    def with_rarity(self, rarity: int) -> Creature:
        """Return a new Creature with a different rarity score."""
        return Creature(self.entity_id, self.group_size, self.active_periods, rarity, self.groups_allowed)
