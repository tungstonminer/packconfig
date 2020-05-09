"""Define various ores from the Advanced Rocketry mod."""

from packconfig.oregen import BiomeSet, Ore, Vein
from packconfig.oregen.data import vanilla


# Biomes ###############################################################################################################

mars_biomes = BiomeSet(
    "advancedrocketry:hotdryrock",
)

moon_biomes = BiomeSet(
    "advancedrocketry:moon",
    "advancedrocketry:moondark",
)

outer_space_biomes = BiomeSet(
    "advancedrocketry:space",
)

volcanic_biomes = BiomeSet(
    "advancedrocketry:volcanic",
    "advancedrocketry:volcanicbarren",
)

vanilla.jungle_biomes.include(
    "advancedrocketry:alien forest"
)

vanilla.oak_forest_biomes.include(
    "advancedrocketry:stormland",
)

vanilla.ocean_biomes.include(
    "advancedrocketry:oceanspires",
)

vanilla.tundra_biomes.include(
    "advancedrocketry:crystalchasms",
)

vanilla.swamp_biomes.include(
    "advancedrocketry:deepswamp",
    "advancedrocketry:marsh",
)


# Ores #################################################################################################################

# Base Materials
basalt = Ore("advancedrocketry:basalt")

# Metals
aluminum_ore = Ore("libvulpes:ore0", 9)
copper_ore = Ore("libvulpes:ore0", 4)
dilithium_ore = Ore("libvulpes:ore0", 0)
iridium_ore = Ore("libvulpes:ore0", 10)
tin_ore = Ore("libvulpes:ore0", 5)
titanium_ore = Ore("libvulpes:ore0", 8)


# Veins#################################################################################################################

aluminum_vein = Vein(aluminum_ore)
copper_vein = Vein(copper_ore)
dilithium_vein = Vein(dilithium_ore)
iridium_vein = Vein(iridium_ore)
tin_vein = Vein(tin_ore)
titanium_vein = Vein(titanium_ore)
