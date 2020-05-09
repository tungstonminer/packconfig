"""Define the MobConfigFile class."""

import json
import os

from io import FileIO
from typing import Any, Dict, Iterable, List, Optional, Union

from packconfig.mobgen import Creature, Spawn
from packconfig.mobgen.spawn import FILLER_MOB


########################################################################################################################

class MobConfigFile(object):
    """MobConfigFile is the base class for an InControl! config files."""

    def __init__(self, target_file: str, *spawns: Iterable[Spawn]):
        """Create a new potential spawn file."""
        self.target_file = target_file
        self.spawns = [s for s in spawns]

    # Properties ###################################################################################

    @property
    def active_spawns(self) -> Iterable[Spawn]:
        """Return all spawns which actively place creatures (i.e., not prohibitions)."""
        for spawn in self.spawns:
            if not spawn.is_prohibition:
                yield spawn

    @property
    def creatures(self) -> Dict[str, Iterable[Creature]]:
        """Isolate the list of creatures used across all spawns."""
        if not hasattr(self, "_creatures"):
            result = {}
            for spawn in self.active_spawns:
                for creature in spawn.creatures:
                    if creature.entity_id not in result:
                        result[creature.entity_id] = []
                    result[creature.entity_id].append(creature)

            self._creatures = result

        return self._creatures

    @property
    def entity_ids(self) -> Iterable[str]:
        """Get all the entity ids mentioned anywhere in these rules."""
        if not hasattr(self, "_entity_ids"):
            result = set()
            for spawn in self.active_spawns:
                for creature in spawn.creatures:
                    if creature.entity_id == FILLER_MOB:
                        continue
                    result.add(creature.entity_id)

            self._entity_ids = sorted(result)

        for entity_id in self._entity_ids:
            yield entity_id

    @property
    def is_empty(self) -> bool:
        """Get wether this config file has any spawns."""
        return len(self.spawns) == 0

    @property
    def prohibitions(self) -> Iterable[str]:
        """Return all spawns which prohibit certain spawn behaviors."""
        for spawn in self.spawns:
            if spawn.is_prohibition:
                yield spawn

    # Public Methods ###############################################################################

    def as_json(self) -> Union[List[Any], Dict[str, Any]]:
        """Convert this file's data into a JSON-able representation."""
        return []

    def write(self, target_dir: Optional[str]):
        """Print a JSON-encoded version of this file."""
        text = json.dumps(self.as_json(), indent="    ")
        if target_dir is not None:
            with FileIO(os.path.join(target_dir, self.target_file), "w") as f:
                f.write(text.encode("utf8"))
        else:
            print(f"{self.target_file} >>>\n{text}\n<<<")
