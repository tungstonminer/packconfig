"""Define the SpawnFile class."""

from collections import namedtuple
from typing import Any, Dict, Iterable, List

from packconfig import Range
from packconfig.mobgen import BiomeSet, Creature, MobConfigFile, Spawn
from packconfig.mobgen.spawn import FILLER_MOB

########################################################################################################################

CreaturePeriod = namedtuple("CreaturePeriod", "period weather structure creature")


########################################################################################################################

class SpawnFile(MobConfigFile):
    """SpawnFile contains rules which evaluate whether or not any given spawn attempt is allowed to succeed."""

    def __init__(self, *spawns: Iterable[Spawn]):
        """Create a new spawn file."""
        super().__init__("spawn.json", *spawns)

    # Public Methods ###############################################################################

    def as_json(self) -> Dict[str, Any]:
        """Convert this file's data into a JSON-able representation."""
        result = []
        self._apply_default_rules(result)
        self._apply_biome_limits(result)
        self._allow_creatures_within_limits(result)
        self._apply_prohibitions(result)
        self._prohibit_all_creatures(result)

        return result

    # Private Methods ##############################################################################

    def _allow_all_creatures(self, rules: List[Dict[str, Any]]):
        rules.append({
            "mob": [e for e in self.entity_ids],
            "result": "allow"
        })

    def _allow_creatures_within_limits(self, rules: List[Dict[str, Any]]):
        spawn: Spawn = None
        for spawn in self.active_spawns:
            creature: Creature = None
            for creature in spawn.creatures:
                period: Range = None
                for period in creature.active_periods:
                    rule = {
                        "mob": creature.entity_id,
                        "dimension": spawn.location.dimension,
                        "biome": list(n for n in spawn.location.biomes.names),
                        "blocks": list(b.name for b in spawn.location.biomes.blocks.ores),
                        "structure": spawn.location.structure,
                        "weather": spawn.location.weather,
                        "minlight": spawn.light.lower,
                        "maxlight": spawn.light.upper,
                        "mintime": period.lower,
                        "maxtime": period.upper,
                        "maxcount": {
                            "mob": creature.entity_id,
                            "amount": creature.group_size.upper * creature.groups_allowed,
                            "perplayer": True
                        },
                        "result": "allow"
                    }

                    if spawn.location.biomes is BiomeSet.ANY:
                        del rule["biome"]

                    if rule["dimension"] is None:
                        del rule["dimension"]

                    if rule["structure"] is None:
                        del rule["structure"]

                    if rule["weather"] is None:
                        del rule["weather"]

                    if rule["minlight"] == 0:
                        del rule["minlight"]

                    if rule["maxlight"] == 15:
                        del rule["maxlight"]

                    if rule["mintime"] == 0:
                        del rule["mintime"]

                    if rule["maxtime"] == 24000:
                        del rule["maxtime"]

                    rules.append(rule)

    def _apply_biome_limits(self, rules: List[Dict[str, Any]]):
        spawn: Spawn = None
        new_rules = []
        for spawn in self.active_spawns:
            if len(list(spawn.creatures)) == 0:
                continue

            rule = {
                "mob": [c.entity_id for c in spawn.creatures],
                "dimension": spawn.location.dimension,
                "biome": list(spawn.location.biomes.names),
                "structure": spawn.location.structure,
                "mincount": {
                    "amount": spawn.limit,
                    "perperson": True,
                    "mob": [c.entity_id for c in spawn.creatures],
                },
                "result": "deny"
            }

            if spawn.location.biomes is BiomeSet.ANY:
                del rule["biome"]

            if rule["dimension"] is None:
                del rule["dimension"]

            if rule["structure"] is None:
                del rule["structure"]

            new_rules.append(rule)

        new_rules = sorted(new_rules, key=(lambda a: a["mincount"]["amount"]), reverse=True)
        rules.extend(new_rules)

    def _apply_default_rules(self, rules: List[Dict[str, Any]]):
        if self.is_empty:
            return

        rules.append({
            "mob": FILLER_MOB,
            "result": "deny",
        })
        rules.append({
            "spawner": True,
            "result": "default",
        })

    def _apply_prohibitions(self, rules: List[Dict[str, Any]]):
        spawn: Spawn = None
        for spawn in self.prohibitions:
            rule = {
                "biome": list(spawn.location.biomes.names),
                "structure": spawn.location.structure,
                "mob": [c.entity_id for c in spawn.creatures],
                "result": "deny",
            }

            if spawn.location.biomes is BiomeSet.ANY:
                del rule["biome"]

            if rule["structure"] is None:
                del rule["structure"]

            rules.append(rule)

    def _gather_creatures_by_period(self) -> Dict[str, List[Creature]]:
        spawn: Spawn = None
        creatures_by_period: Dict[str, List[Creature]] = {}
        for spawn in self.active_spawns:
            creature: Creature = None
            for creature in spawn.creatures:
                period: Range = None
                for period in creature.active_periods:
                    weather = spawn.location.weather
                    weather = weather if weather is not None else "zzz"
                    structure = spawn.location.structure
                    structure = structure if structure is not None else "zzz"
                    key = f"{weather}_{period.lower}_{period.upper}"

                    if key not in creatures_by_period:
                        creatures_by_period[key] = set()

                    creatures_by_period[key].add(CreaturePeriod(
                        period, spawn.location.weather, spawn.location.structure, creature
                    ))

        return creatures_by_period

    def _prohibit_all_creatures(self, rules: List[Dict[str, Any]]):
        entity_ids = [e for e in self.entity_ids]
        if len(entity_ids) == 0:
            return

        rules.append({
            "mob": entity_ids,
            "result": "deny"
        })
