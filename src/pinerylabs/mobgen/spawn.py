"""Define the Spawn class."""

from typing import Iterable, Optional

from pinerylabs.mobgen import Creature, Location, Range


########################################################################################################################

DEFAULT_CYCLE_LENGTH = 60
FILLER_MOB = "minecraft:giant"
TICKS_PER_SECOND = 20


########################################################################################################################

class Spawn(object):
    """Spawn represents some condition under which creatures are placed in the world."""

    def __init__(
        self,
        location: Location,
        *creatures: Iterable[Creature],
        light: Optional[Range] = None,
        limit: Optional[int] = None,
        cycle_length: Optional[int] = None,
        altitude: Optional[Range] = None,
    ):
        """
        Create a new spawn.

        Creatures from the given list are randomly spawned at the given rate until the limit is reached. The creatures
        are spawned in accordance with their group sizes, one group at a time, until that limit is reached.  As
        creatures disappear or are killed, they will be replenished at the given rate.

        Arguments:
            location: a Location where this spawn occurs
            creatures: the list of creatures to be spawned
            light: the amount of light permitted for this spawn
            limit: the maximum number of creatures which spawn will create at once. If none is given, then the upper
                limit of the largest creature group will be used
            cycle_length: the approximate number of seconds it should take a creature with a rarity of 1 to appear.
                Creatures with rarity `r` will appear in `1/r` this amount of time.

        """
        self.altitude = altitude
        self.location = location
        self.creatures = creatures
        self.light = light
        self.limit = limit
        self.cycle_length = cycle_length if cycle_length is not None else DEFAULT_CYCLE_LENGTH

        if self.altitude is None:
            self.altitude = Range(0, 256)

        if self.light is None:
            self.light = Range(0, 15)

    # Properties ###################################################################################

    @property
    def creatures(self) -> Iterable[Creature]:
        """Get the creatures which spawn at this location."""
        for creature in self._creatures:
            yield creature

    @creatures.setter
    def creatures(self, creatures: Iterable[Creature]):
        self._creatures = [c for c in creatures]

    @property
    def is_empty(self) -> bool:
        """Get whether this spawn has no creatures in it."""
        return len(self._creatures) == 0

    @property
    def is_prohibition(self) -> bool:
        """Return whether this spawn object describes a prohibited spawn (i.e., limit == 0)."""
        return self.limit == 0

    @property
    def limit(self) -> int:
        """Get the maximum number of creatures to allow at one time from this spawn."""
        if self._limit is not None:
            return self._limit

        result = 1
        creature: Creature = None
        for creature in self.creatures:
            result += creature.max_individuals

        return result

    @limit.setter
    def limit(self, value: Optional[int]):
        self._limit = value

    # Public Methods ###############################################################################

    def add_creature(self, creature: Creature):
        """Add a creature to this spawn."""
        self._creatures.append(creature)

    def compute_filler_mob(self) -> Creature:
        """Create a Creature to pad the remainder of the spawn opportunities up to the total slots."""
        total_used = 0
        for creature in self.creatures:
            total_used += creature.rarity

        spawn_points = TICKS_PER_SECOND * self.cycle_length
        if total_used >= spawn_points:
            return None

        return Creature(FILLER_MOB, rarity=(spawn_points - total_used))
