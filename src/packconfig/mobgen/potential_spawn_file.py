"""Define the PotentialSpawnFile class."""

from typing import Any, Dict, List, Iterable

from packconfig.mobgen import BiomeSet, MobConfigFile, Spawn


########################################################################################################################

class PotentialSpawnFile(MobConfigFile):
    """PotentialSpawnFile adds new spawn attempts which weren't already in the game."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new potential spawn file."""
        super().__init__("potentialspawn.json", *spawns)

    # Public Methods ###############################################################################

    def as_json(self) -> Dict[str, Any]:
        """Convert this file's data into a JSON-able representation."""
        result = []
        self._add_removes(result)
        self._add_spawns(result)
        return result

    def _add_removes(self, rules: List[Dict[str, Any]]):
        entity_ids = [e for e in self.entity_ids]
        if len(entity_ids) > 0:
            rules.append({
                "remove": [e for e in self.entity_ids]
            })

    def _add_spawns(self, rules: List[Dict[str, Any]]):
        spawn: Spawn = None
        for spawn in self.spawns:
            if spawn.is_prohibition:
                continue

            creatures = list(spawn.creatures)
            if len(creatures) == 0:
                continue

            mobs = []

            filler_mob = spawn.compute_filler_mob()
            if filler_mob is not None:
                mobs.append({
                    "mob": filler_mob.entity_id,
                    "weight": filler_mob.rarity,
                })

            for creature in creatures:
                mobs.append({
                    "mob": creature.entity_id,
                    "groupcountmin": creature.group_size.lower,
                    "groupcountmax": creature.group_size.upper,
                    "weight": creature.rarity,
                })

            if isinstance(spawn.location.biomes, str):
                print(f"invalid spawn: {spawn.location.biomes}")

            entry = {
                "biome": list(spawn.location.biomes.names),
                "structure": spawn.location.structure,
                "block": [b.name for b in spawn.location.biomes.blocks.ores],
                "seesky": not spawn.location.biomes.underground,
                "weather": spawn.location.weather,
                "minheight": spawn.altitude.lower,
                "maxheight": spawn.altitude.upper,
                "mobs": mobs,
            }

            if spawn.location.biomes is BiomeSet.ANY:
                del entry["biome"]

            if entry["minheight"] == 0:
                del entry["minheight"]

            if entry["maxheight"] == 256:
                del entry["maxheight"]

            if entry["seesky"] is True:
                del entry["seesky"]

            if entry["structure"] is None:
                del entry["structure"]

            if entry["weather"] is None:
                del entry["weather"]

            rules.append(entry)
