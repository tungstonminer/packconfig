"""Define the Loot class."""

from typing import Iterable


########################################################################################################################

class Loot(object):
    """Loot defines objects dropped by mobs when killed."""

    def __init__(self, count: str, *items: Iterable[str]):
        """Create a new loot."""
        self.count = count
        self.items = list(items)
