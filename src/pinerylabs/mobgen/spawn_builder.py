"""Define the SpawnBuilder class."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterable, Optional

from pinerylabs.mobgen import Creature, Location, Range, Spawn


########################################################################################################################

class SpawnBuilder(object):
    """SpawnBuilder aids in building a spawn list by offering various contextual wrappers."""

    def __init__(self):
        """Create a new spawn builder."""
        self._active_periods = None
        self._altitude = None
        self._current_spawn = None
        self._light = None
        self._location = None
        self._spawns = []

    # Properties ###################################################################################

    @property
    def spawns(self) -> Iterable[Spawn]:
        """Get the list of spawns created with this builder."""
        spawn: Spawn = None
        for spawn in self._spawns:
            if not spawn.is_empty:
                yield spawn

    # Public Methods ###############################################################################

    def add(self, creature: Creature):
        """Add a new spawn to the list, applying any overrides currently in effect."""
        if self._current_spawn is None:
            raise RuntimeError("cannot add a creature without a spawn")

        active_periods = self._active_periods
        if active_periods is None:
            active_periods = [Range(0, 24000)]

        self._current_spawn.add_creature(creature.with_active_periods(*self._active_periods))

    # Context Managers #############################################################################

    @contextmanager
    def active_periods(self, active_periods: Iterable[Range]) -> SpawnBuilder:
        """Override the active periods of spawns created in this block."""
        if self._current_spawn:
            raise RuntimeError("cannot change active periods once a spawn is in progress")

        self._active_periods = [p.clone() for p in active_periods]
        try:
            yield self
        finally:
            self._active_periods = None

    @contextmanager
    def altitude(self, lower: int = 0, upper: int = 256) -> SpawnBuilder:
        """Override the altitude of spawns created in this block."""
        if self._current_spawn:
            raise RuntimeError("cannot change altitude once a spawn is in progress")

        self._altitude = Range(lower, upper)
        try:
            yield self
        finally:
            self._altitude = None

    @contextmanager
    def light(self, lower: int = 0, upper: int = 15) -> SpawnBuilder:
        """Overright the light level of spawns created in this block."""
        if self._current_spawn:
            raise RuntimeError("cannot change light level once a spawn is in progress")

        self._light = Range(lower, upper)
        try:
            yield self
        finally:
            self._light = None

    @contextmanager
    def location(self, location: Location) -> SpawnBuilder:
        """Override the location of spawns created in this block."""
        if self._current_spawn:
            raise RuntimeError("cannot change locations once a spawn is in progress")

        self._location = location
        try:
            yield self
        finally:
            self._location = None

    @contextmanager
    def spawn(self, limit: Optional[int] = None, cycle_length: Optional[int] = None):
        """Start a new spawn."""
        if self._active_periods is None:
            raise RuntimeError("cannot start a spawn with active periods")

        if self._location is None:
            raise RuntimeError("cannot start a spawn without a location")

        self._current_spawn = Spawn(
            self._location, light=self._light, limit=limit, cycle_length=cycle_length, altitude=self._altitude
        )
        try:
            yield self
        finally:
            self._spawns.append(self._current_spawn)
            self._current_spawn = None

    # Magic Methods ################################################################################

    def __enter__(self) -> SpawnBuilder:
        """Begin a context with this file."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Exit the context using this file."""
        return False
