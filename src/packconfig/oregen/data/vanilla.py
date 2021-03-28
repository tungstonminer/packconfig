"""Define various materials from vanilla Minecraft."""

from packconfig.oregen import BiomeSet, Ore, Vein
from packconfig.oregen.distributions import NormalDistribution, UniformDistribution


# Biomes ###############################################################################################################

# Base Biome Sets ##################################################################################

any_biome = BiomeSet.ANY

birch_forest_biomes = BiomeSet(
    "minecraft:birch_forest",
    "minecraft:birch_forest_hills",
)

desert_biomes = BiomeSet(
    "minecraft:desert",
    "minecraft:desert_hills",
    "minecraft:mutated_desert",
)

jungle_biomes = BiomeSet(
    "minecraft:jungle",
    "minecraft:jungle_edge",
    "minecraft:jungle_hills",
)

mesa_biomes = BiomeSet(
    "minecraft:mesa",
    "minecraft:mesa_clear_rock",
    "minecraft:mesa_rock",
    "minecraft:mutated_mesa",
    "minecraft:mutated_mesa_clear_rock",
    "minecraft:mutated_mesa_rock"
)

mountain_biomes = BiomeSet(
    "minecraft:extreme_hills",
    "minecraft:extreme_hills_with_trees",
    "minecraft:ice_mountains",
    "minecraft:mutated_extreme_hills",
    "minecraft:smaller_extreme_hills",
)

mushroom_biomes = BiomeSet(
    "minecraft:mushroom_island",
    "minecraft:mushroom_island_shore",
)

nether_biomes = BiomeSet(
    "minecraft:hell"
)

oak_forest_biomes = BiomeSet(
    "minecraft:forest",
    "minecraft:forest_hills",
    "minecraft:mutated_forest"
)

ocean_biomes = BiomeSet(
    "minecraft:deep_ocean",
    "minecraft:frozen_ocean",
    "minecraft:ocean"
)

plains_biomes = BiomeSet(
    "minecraft:mutated_plains",
    "minecraft:plains"
)

redwood_forest_biomes = BiomeSet(
    "minecraft:redwood_taiga",
    "minecraft:redwood_taiga_hills"
)

river_biomes = BiomeSet(
    "minecraft:frozen_river",
    "minecraft:river",
)

roofed_forest_biomes = BiomeSet(
    "minecraft:roofed_forest",
)

savanna_biomes = BiomeSet(
    "minecraft:mutated_savanna",
    "minecraft:mutated_savanna_rock",
    "minecraft:savanna",
    "minecraft:savanna_rock",
)

shore_biomes = BiomeSet(
    "minecraft:beaches",
    "minecraft:cold_beach",
    "minecraft:stone_beach",
)

spruce_forest_biomes = BiomeSet(
    "minecraft:taiga",
    "minecraft:taiga_cold",
    "minecraft:taiga_cold_hills",
    "minecraft:taiga_hills",
)

swamp_biomes = BiomeSet(
    "minecraft:swampland"
)

the_end_biomes = BiomeSet(
    "minecraft:sky"
)

tundra_biomes = BiomeSet(
    "minecraft:ice_flats",
    "minecraft:ice_mountains"
)

# Feature-oriented Biome Sets ######################################################################

flowery_biomes = BiomeSet(
    "minecraft:mutated_forest",
    "minecraft:mutated_plains"
)

forested_biomes = BiomeSet().add(
    birch_forest_biomes,
    jungle_biomes,
    oak_forest_biomes,
    redwood_forest_biomes,
    roofed_forest_biomes,
    spruce_forest_biomes,
)

gravelly_biomes = BiomeSet(
    "minecraft:cold_beach",
    "minecraft:deep_ocean",
    "minecraft:frozen_ocean",
    "minecraft:ocean",
    "minecraft:frozen_river",
    "minecraft:river",
)

hilly_biomes = BiomeSet(
    "minecraft:desert_hills",
    "minecraft:birch_forest_hills",
    "minecraft:forest_hills",
    "minecraft:jungle_hills",
    "minecraft:redwood_taiga_hills",
    "minecraft:taiga_cold_hills",
    "minecraft:taiga_hills",
)

snowy_biomes = BiomeSet(
    "minecraft:froze_river",
    "minecraft:frozen_ocean",
    "minecraft:ice_flats",
    "minecraft:ice_mountains",
    "minecraft:taiga_cold",
    "minecraft:taiga_cold_hills",
)

# Computed Biome Sets ##############################################################################

all_biomes = BiomeSet.all_biomes()

earth_biomes = BiomeSet().add(all_biomes).remove(nether_biomes, the_end_biomes)

water_biomes = BiomeSet().add(ocean_biomes, river_biomes)
land_biomes = BiomeSet().add(earth_biomes).remove(water_biomes)

cold_biomes = BiomeSet().add(snowy_biomes)
hot_biomes = BiomeSet().add(desert_biomes, savanna_biomes, jungle_biomes)
warm_biomes = BiomeSet().add(earth_biomes).remove(cold_biomes, hot_biomes)

dry_biomes = BiomeSet().add(desert_biomes, mesa_biomes, savanna_biomes)
wet_biomes = BiomeSet().add(jungle_biomes, mushroom_biomes, swamp_biomes)
damp_biomes = BiomeSet().add(earth_biomes).remove(dry_biomes, wet_biomes)

high_biomes = BiomeSet().add(hilly_biomes, mountain_biomes, mesa_biomes, mushroom_biomes)
deep_biomes = BiomeSet().add(ocean_biomes)
low_biomes = BiomeSet().add(earth_biomes).remove(high_biomes, deep_biomes)


# Dimensions ##########3################################################################################################

overworld = 0
nether = -1
the_end = 1


# Distributions ########################################################################################################

anywhere_band = UniformDistribution("anywhere", 0, 256)
coal_band = UniformDistribution("coal_band", 0, 128)
diamond_band = UniformDistribution("diamond_band", 0, 16)
emerald_band = UniformDistribution("emerald_band", 4, 28)
gold_band = UniformDistribution("gold_band", 0, 32)
iron_band = UniformDistribution("iron_band", 0, 64)
lapis_band = NormalDistribution("lapis_band", 16, 16)
mesa_band = UniformDistribution("mesa_band", 32, 80)
quartz_band = UniformDistribution("quartz_band", 10, 118)
stone_variants_band = UniformDistribution("stone_variants_band", 0, 80)


# Ores #################################################################################################################

# Common Materials
andesite = Ore("minecraft:stone", variant="andesite")
bedrock = Ore("minecraft:bedrock")
bone = Ore("minecraft:bone_block")
clay = Ore("minecraft:clay")
cobblestone = Ore("minecraft:cobblestone")
diorite = Ore("minecraft:stone", variant="diorite")
dirt = Ore("minecraft:dirt")
endstone = Ore("minecraft:end_stone")
granite = Ore("minecraft:stone", variant="granite")
grass = Ore("minecraft:grass")
gravel = Ore("minecraft:gravel")
ice = Ore("minecraft:ice")
mycelium = Ore("minecraft:mycelium")
netherrack = Ore("minecraft:netherrack")
nether_brick = Ore("minecraft:nether_brick")
obsidian = Ore("minecraft:obsidian")
planks = Ore("minecraft:planks")
podzol = Ore("minecraft:podzol")
red_sand = Ore("minecraft:sand", 1)
red_sandstone = Ore("minecraft:red_sandstone")
sandstone = Ore("minecraft:sandstone")
sand = Ore("minecraft:sand")
snow = Ore("minecraft:snow")
soul_sand = Ore("minecraft:soul_sand")
stone = Ore("minecraft:stone")

# Liquids
air = Ore("minecraft:air")
lava = Ore("minecraft:lava")
water = Ore("minecraft:water")

# Metals
gold_ore = Ore("minecraft:gold_ore")
iron_ore = Ore("minecraft:iron_ore")

# Minerals
coal_ore = Ore("minecraft:coal_ore")
diamond_ore = Ore("minecraft:diamond_ore")
emerald_ore = Ore("minecraft:emerald_ore")
glowstone = Ore("minecraft:glowstone")
lapis_ore = Ore("minecraft:lapis_ore")
magma = Ore("minecraft:magma")
quartz_ore = Ore("minecraft:quartz_ore")
redstone_ore = Ore("minecraft:redstone_ore")

# Animals
silverfish = Ore("minecraft:monster_egg", variant="stone")


# Veins ################################################################################################################

coal_vein = Vein(coal_ore)
diamond_vein = Vein(diamond_ore)
emerald_vein = Vein(emerald_ore)
gold_vein = Vein(gold_ore)
iron_vein = Vein(iron_ore)
lapis_vein = Vein(lapis_ore)
quartz_vein = Vein(quartz_ore, material_ore=netherrack)
redstone_vein = Vein(redstone_ore)
silverfish_vein = Vein(silverfish)
