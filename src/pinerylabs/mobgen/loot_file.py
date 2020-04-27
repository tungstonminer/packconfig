"""Define the LootFile class."""

import re

from typing import Any, Dict, Iterable, List, Union

from pinerylabs.mobgen import Creature, MobConfigFile, Spawn


########################################################################################################################

class LootFile(MobConfigFile):
    """LootFile defines what loot you get from killing certain creatures."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new config file."""
        super().__init__("loot.json", *spawns)

    # Public Methods ###############################################################################

    def as_json(self) -> Union[List[Any], Dict[str, Any]]:
        """Convert this file's data into a JSON-able representation."""
        result = []
        creature: Creature = None
        for creatures in self.creatures.values():
            creature = creatures[0]
            if creature.loot_list is None:
                continue

            result.append({
                "mob": creature.entity_id,
                "removeall": True,
            })
            for loot in creature.loot_list:
                result.append({
                    "mob": creature.entity_id,
                    "item": [self._convert_item(item) for item in loot.items],
                    "itemcount": loot.count,
                })

        return result

    # Private Methods ##############################################################################

    def _convert_item(self, item_text: str) -> Union[str, Dict[str, Any]]:
        match = re.match("(?P<mod>[^:]*):(?P<item>[^:]*):(?P<meta>.*)", item_text)
        if match is not None:
            return f"{match.group('mod')}:{match.group('item')}@{match.group('meta')}"

        return item_text
