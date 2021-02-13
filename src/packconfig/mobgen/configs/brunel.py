"""Define the entity generation settings for Brunel 3."""

from packconfig import Range
from packconfig.mobgen import BiomeSet, Loot
from packconfig.oregen import OreList
from packconfig.oregen.data import vanilla as mc


# Activity Ranges ######################################################################################################

ANY = [Range(0, 24000)]
DAY = [Range(23500, 24000), Range(0, 12500)]
NIGHT = [Range(11500, 24000), Range(0, 500)]
DAWN = [Range(11000, 13000)]
DUSK = [Range(0, 1000), Range(23000, 24000)]

TWILIGHT = DAWN + DUSK


# Group Size Presets ###################################################################################################

LONER = Range(1, 1)
PAIR = Range(1, 2)
CLUSTER = Range(2, 3)
TROOP = Range(3, 6)
HERD = Range(6, 10)
SWARM = Range(10, 20)


# Spawn Block Sets #####################################################################################################

AERIAL = OreList(mc.air)
AQUATIC = OreList(mc.water)
CARPETED = OreList(mc.grass, mc.dirt, mc.sand)
FUNGAL = OreList(mc.mycelium)
GRASSY = OreList(mc.grass, mc.dirt, mc.sand)
GRAVELLY = OreList(mc.gravel, mc.dirt, mc.sand)
HELLISH = OreList(mc.netherrack, mc.soul_sand, mc.nether_brick, mc.bedrock)
MOLTEN = OreList(mc.lava)
SANDY = OreList(mc.dirt, mc.sand, mc.sandstone)
SNOWY = OreList(mc.dirt, mc.gravel, mc.ice, mc.sand, mc.snow)
STONY = OreList(mc.cobblestone, mc.stone)
SWAMPY = OreList(mc.dirt, mc.grass, mc.sand, mc.water)


# Biome Sets ###########################################################################################################

beach_cold = BiomeSet("Cold Beach", blocks=SNOWY)
beach_sandy = BiomeSet("Beach", blocks=OreList(mc.grass, mc.sand))
beach_gravel = BiomeSet("OceanSpires", "Stone Beach", blocks=GRAVELLY)
desert = BiomeSet("Desert", "Desert M", "DesertHills", blocks=SANDY)
forest_canopy = BiomeSet("Roofed Forest", "Roofed Forest M", blocks=CARPETED)
forest_ice = BiomeSet("Ice Plains Spikes", blocks=SNOWY)
forest_temperate = BiomeSet(
    "Birch Forest", "Birch Forest M", "Birch Forest Hills", "Birch Forest Hills M", "Flower Forest", "Forest",
    "ForestHills", blocks=CARPETED
)
forest_jungle = BiomeSet("Jungle", "Jungle M", "JungleEdge", "JungleEdge M", "JungleHills", blocks=CARPETED)
mars = BiomeSet("NotDryRock", blocks=None)
mesa = BiomeSet(
    "Mesa", "Mesa (Bryce)", "Mesa Plateau", "Mesa Plateau F", "Mesa Plateau F M", "Mesa Plateau M",
    blocks=OreList(mc.red_sand, mc.red_sandstone, mc.dirt, mc.grass)
)
mountain = BiomeSet("Extreme Hills", "Extreme Hills M", "Extreme Hills Edge", blocks=GRASSY)
mountain_forest = BiomeSet("Extreme Hills+", "Extreme Hills+ M", blocks=GRASSY)
moon = BiomeSet("Moon", "MoonDark", blocks=None)
mushroom = BiomeSet("MushroomIsland", "MushroomIslandShore", blocks=FUNGAL)
nether = BiomeSet("Hell", blocks=HELLISH)
ocean = BiomeSet("Ocean", blocks=AQUATIC)
ocean_deep = BiomeSet("Deep Ocean", blocks=AQUATIC)
ocean_frozen = BiomeSet("FrozenOcean", blocks=AQUATIC)
plains = BiomeSet("Plains", "Sunflower Plains", blocks=GRASSY)
river = BiomeSet("River", blocks=OreList(mc.grass, mc.sand))
river_frozen = BiomeSet("FrozenRiver", blocks=OreList.merge(SNOWY, GRASSY))
savanna = BiomeSet("Savanna", "Savanna M", "Savanna Plateau", "Savanna Plateau M", blocks=GRASSY)
space = BiomeSet("Space", "The Void", blocks=AERIAL)
swamp = BiomeSet("DeepSwamp", "Marsh", "Swampland", "Swampland M", blocks=SWAMPY)
taiga = BiomeSet(
    "Mega Spruce Taiga", "Mega Taiga", "Mega Taiga Hills", "Redwood Taiga Hills M", "Taiga", "Taiga M", "TaigaHills",
    blocks=CARPETED
)
taiga_snowy = BiomeSet("Cold Taiga", "Cold Taiga M", "Cold Taiga Hills", blocks=CARPETED)
the_end = BiomeSet("The End", blocks=mc.endstone)
tundra = BiomeSet("CrystalChasms", "Ice Plains", "Ice Mountains", blocks=SNOWY)
volcanic = BiomeSet("Stormland", "Volcanic", "VolcanicBarren", blocks=STONY)

earth = BiomeSet.merge(
    beach_cold, beach_sandy, beach_gravel, desert, forest_canopy, forest_ice, forest_temperate, forest_jungle,
    mountain, mountain_forest, mushroom, ocean, ocean_deep, ocean_frozen, plains, river, river_frozen, savanna, swamp,
    taiga, taiga_snowy, tundra
)
settled = BiomeSet.merge(
    beach_sandy, desert, forest_canopy, forest_temperate, plains, river, savanna, taiga, taiga_snowy, swamp
)


# Loot Items  ##########################################################################################################

blaze_powder = "minecraft:blaze_powder"
blaze_rod = "minecraft:blaze_rod"
bone = "minecraft:bone"
bottle_o_enchanting = "minecraft:experience_bottle"
carcass_chicken = "minecraft:chicken"
carcass_chicken_prime = "animania:raw_prime_chicken"
carcass_clownfish = "minecraft:fish:2"
carcass_crab = "betteranimalsplus:crab_meat_raw"
carcass_crab = "harvestcraft:crabrawitem"
carcass_eel = "harvestcraft:eelrawitem"
carcass_fish = "minecraft:fish"
carcass_frog = "harvestcraft:frograwitem"
carcass_octopus = "harvestcraft:octopusrawitem"
carcass_peacock = "animania:raw_peacock"
carcass_peacock_prime = "animania:raw_prime_peacock"
carcass_pheasant = "betteranimalsplus:pheasantraw"
carcass_pufferfish = "minecraft:fish:3"
carcass_rabbit = "minecraft:rabbit"
carcass_rabbit_prime = "animania:raw_prime_rabbit"
carcass_salmon = "minecraft:fish:1"
carcass_squid = "harvestcraft:calamarirawitem"
egg_chicken_brown = "animania:brown_egg"
egg_chicken_white = "minecraft:egg"
egg_goose = "betteranimalsplus:goose_egg"
egg_goose_golden = "betteranimalsplus:golden_goose_egg"
egg_peafowl_egg_blue = "animania:peacock_egg_blue"
egg_peafowl_egg_white = "animania:peacock_egg_white"
egg_pheasant = "betteranimalsplus:pheasant_egg"
egg_turkey = "betteranimalsplus:turkey_egg"
emerald = "minecraft:emerald"
ender_pearl = "minecraft:ender_pearl"
feather_chicken_white = "minecraft:feather"
feather_peacock_blue = "animania:blue_peacock_feather"
feather_peacock_charcoal = "animania:charcoal_peacock_feather"
feather_peacock_opal = "animania:opal_peacock_feather"
feather_peacock_peach = "animania:peach_peacock_feather"
feather_peacock_purple = "animania:purple_peacock_feather"
feather_peacock_taupe = "animania:taupe_peacock_feather"
feather_peacock_white = "animania:white_peacock_feather"
fire_charge = "minecraft:fire_charge"
foliaath_seed = "mowziesmobs:foliaath_seed"
ghast_tear = "minecraft:ghast_tear"
gunpowder = "minecraft:gunpowder"
hide_large = "minecraft:leather"
hide_small = "minecraft:rabbit_hide"
fur_black = "betteranimalsplus:bear_skin_black"
fur_brown = "betteranimalsplus:bear_skin_brown"
fur_white = "betteranimalsplus:bear_skin_white"
ink_sac = "minecraft:dye"
iron_block = "minecraft:iron_block"
iron_ingot = "minecraft:iron_ingot"
iron_nugget = "minecraft:iron_nugget"
kale = "harvestcraft:kaleitem"
luminous_jelly = "mowziesmobs:glowing_jelly"
magma_cream = "minecraft:magma_cream"
meat_beef = "minecraft:beef"
meat_beef_prime = "animania:raw_prime_beef"
meat_chevon = "animania:raw_chevon"
meat_chevon_prime = "animania:raw_prime_chevon"
meat_duck = "harvestcraft:duckrawitem"
meat_eel = "betteranimalsplus:eel_meat_raw"
meat_fish = "harvestcraft:groundfishitem"
meat_frog = "animania:raw_frog_legs"
meat_horse = "animania:raw_horse"
meat_mutton = "minecraft:mutton"
meat_mutton_prime = "animania:raw_prime_mutton"
meat_pork = "minecraft:porkchop"
meat_pork_prime = "animania:raw_prime_pork"
meat_turkey_body = "betteranimalsplus:turkey_raw"
meat_turkey_leg = "betteranimalsplus:turkey_leg_raw"
meat_venison = "betteranimalsplus:venisonraw"
meat_venison = "harvestcraft:venisonrawitem"
mushroom_item = "minecraft:red_mushroom"
naga_fang = "mowziesmobs:naga_fang"
rabbit_foot = "minecraft:rabbit_foot"
rabbit_foot = "minecraft:rabbit_foot"
slime = "minecraft:slime_ball"
spider_eye = "minecraft:spider_eye"
turkey_meat = "harvestcraft:turkeyrawitem"
turtle_carcass = "harvestcraft:turtlerawitem"
wool = "minecraft:wool"


# Loot Lists ###########################################################################################################

bear_black_loot = [Loot("1-2", fur_black)]
bear_brown_loot = [Loot("1-2", fur_brown)]
bird_raptor_loot = []
bird_tiny_loot = []
blaze_loot = [Loot("1-3", blaze_rod), Loot("1-3", blaze_powder)]
boar_loot = [Loot("2-4", meat_pork), Loot("0-1", hide_large)]
bovine_bull_loot = []
bovine_calf_loot = []
bovine_cow_loot = []
chicken_chick_loot = []
chicken_hen_loot = []
chicken_rooster_loot = []
default_loot = None
eel_loot = []
enderman_loot = []
equine_loot = []
foliaath_loot = []
ghast_loot = []
goat_buck_loot = []
goat_doe_loot = []
goose_loot = []
horse_foal_loot = []
horse_mare_loot = []
horse_stallion_loot = []
horseshoecrab_loot = []
jellyfish_loot = []
lantern_loot = []
large_fish_loot = []
llama_loot = []
magma_cube_loot = []
mammal_huge_loot = []
mammal_medium_loot = []
mammal_small_loot = [Loot("1", meat_chevon)]
naga_loot = []
nautilus_loot = []
no_loot = []
ocelot_loot = []
porcine_hog_loot = []
porcine_piglet_loot = []
porcine_sow_loot = []
rabbit_doe_loot = []
rabbit_jack_loot = []
rabbit_kit_loot = []
sheep_ewe_loot = []
sheep_kid_loot = []
sheep_ram_loot = []
spider_loot = []
wolf_loot = []
fish_large_loot = []
bovine_mooshroom_loot = []
peafowl_blue_chick_loot = []
peafowl_blue_hen_loot = []
peafowl_blue_cock_loot = []
peafowl_blue_chick_loot = []
peafowl_blue_hen_loot = []
peafowl_blue_cock_loot = []


# Entities #############################################################################################################

# badger = Creature("betteranimalsplus:badger", CLUSTER, loot_list=mammal_small_loot)
# bat = Creature("minecraft:bat", CLUSTER, loot_list=no_loot)
# blackbear = Creature("betteranimalsplus:blackbear", CLUSTER, loot_list=black_bear_loot)
# blaze = Creature("minecraft:blaze", CLUSTER, loot_list=blaze_loot)
# boar = Creature("betteranimalsplus:boar", CLUSTER, loot_list=boar_loot)
# bobbit_worm = Creature("betteranimalsplus:bobbit_worm", CLUSTER, loot_list=no_loot)
# brownbear = Creature("betteranimalsplus:brownbear", CLUSTER, loot_list=bear_brown_loot)
# buck_alpine = Creature("animania:buck_alpine", CLUSTER, loot_list=default_loot)
# buck_angora = Creature("animania:buck_angora", CLUSTER, loot_list=default_loot)
# buck_chinchilla = Creature("animania:buck_chinchilla", CLUSTER, loot_list=default_loot)
# buck_cottontail = Creature("animania:buck_cottontail", CLUSTER, loot_list=default_loot)
# buck_dutch = Creature("animania:buck_dutch", CLUSTER, loot_list=default_loot)
# buck_fainting = Creature("animania:buck_fainting", CLUSTER, loot_list=default_loot)
# buck_havana = Creature("animania:buck_havana", CLUSTER, loot_list=default_loot)
# buck_jack = Creature("animania:buck_jack", CLUSTER, loot_list=default_loot)
# buck_kiko = Creature("animania:buck_kiko", CLUSTER, loot_list=default_loot)
# buck_kinder = Creature("animania:buck_kinder", CLUSTER, loot_list=default_loot)
# buck_lop = Creature("animania:buck_lop", CLUSTER, loot_list=default_loot)
# buck_new_zealand = Creature("animania:buck_new_zealand", CLUSTER, loot_list=default_loot)
# buck_nigerian_dwarf = Creature("animania:buck_nigerian_dwarf", CLUSTER, loot_list=default_loot)
# buck_pygmy = Creature("animania:buck_pygmy", CLUSTER, loot_list=default_loot)
# buck_rex = Creature("animania:buck_rex", CLUSTER, loot_list=default_loot)
# bull_angus = Creature("animania:bull_angus", CLUSTER, loot_list=default_loot)
# bull_friesian = Creature("animania:bull_friesian", CLUSTER, loot_list=default_loot)
# bull_hereford = Creature("animania:bull_hereford", CLUSTER, loot_list=default_loot)
# bull_highland = Creature("animania:bull_highland", CLUSTER, loot_list=default_loot)
# bull_holstein = Creature("animania:bull_holstein", CLUSTER, loot_list=default_loot)
# bull_jersey = Creature("animania:bull_jersey", CLUSTER, loot_list=default_loot)
# bull_longhorn = Creature("animania:bull_longhorn", CLUSTER, loot_list=default_loot)
# bull_mooshroom = Creature("animania:bull_mooshroom", CLUSTER, loot_list=default_loot)
# calf_angus = Creature("animania:calf_angus", CLUSTER, loot_list=default_loot)
# calf_friesian = Creature("animania:calf_friesian", CLUSTER, loot_list=default_loot)
# calf_hereford = Creature("animania:calf_hereford", CLUSTER, loot_list=default_loot)
# calf_highland = Creature("animania:calf_highland", CLUSTER, loot_list=default_loot)
# calf_holstein = Creature("animania:calf_holstein", CLUSTER, loot_list=default_loot)
# calf_jersey = Creature("animania:calf_jersey", CLUSTER, loot_list=default_loot)
# calf_longhorn = Creature("animania:calf_longhorn", CLUSTER, loot_list=default_loot)
# calf_mooshroom = Creature("animania:calf_mooshroom", CLUSTER, loot_list=default_loot)
# cave_spider = Creature("minecraft:cave_spider", CLUSTER, loot_list=default_loot)
# chick_leghorn = Creature("animania:chick_leghorn", CLUSTER, loot_list=default_loot)
# chick_orpington = Creature("animania:chick_orpington", CLUSTER, loot_list=default_loot)
# chick_plymouth_rock = Creature("animania:chick_plymouth_rock", CLUSTER, loot_list=default_loot)
# chick_rhode_island_red = Creature("animania:chick_rhode_island_red", CLUSTER, loot_list=default_loot)
# chick_wyandotte = Creature("animania:chick_wyandotte", CLUSTER, loot_list=default_loot)
# chicken = Creature("minecraft:chicken", CLUSTER, loot_list=default_loot)
# cow = Creature("minecraft:cow", CLUSTER, loot_list=default_loot)
# cow_angus = Creature("animania:cow_angus", CLUSTER, loot_list=default_loot)
# cow_friesian = Creature("animania:cow_friesian", CLUSTER, loot_list=default_loot)
# cow_hereford = Creature("animania:cow_hereford", CLUSTER, loot_list=default_loot)
# cow_highland = Creature("animania:cow_highland", CLUSTER, loot_list=default_loot)
# cow_holstein = Creature("animania:cow_holstein", CLUSTER, loot_list=default_loot)
# cow_jersey = Creature("animania:cow_jersey", CLUSTER, loot_list=default_loot)
# cow_longhorn = Creature("animania:cow_longhorn", CLUSTER, loot_list=default_loot)
# cow_mooshroom = Creature("animania:cow_mooshroom", CLUSTER, loot_list=default_loot)
# coyote = Creature("betteranimalsplus:coyote", CLUSTER, loot_list=default_loot)
# crab = Creature("betteranimalsplus:crab", CLUSTER, loot_list=default_loot)
# creeper = Creature("minecraft:creeper", CLUSTER, loot_list=default_loot)
# dartfrog = Creature("animania:dartfrog", CLUSTER, loot_list=default_loot)
# deer = Creature("betteranimalsplus:deer", CLUSTER, loot_list=default_loot)
# doe_alpine = Creature("animania:doe_alpine", CLUSTER, loot_list=default_loot)
# doe_angora = Creature("animania:doe_angora", CLUSTER, loot_list=default_loot)
# doe_chinchilla = Creature("animania:doe_chinchilla", CLUSTER, loot_list=default_loot)
# doe_cottontail = Creature("animania:doe_cottontail", CLUSTER, loot_list=default_loot)
# doe_dutch = Creature("animania:doe_dutch", CLUSTER, loot_list=default_loot)
# doe_fainting = Creature("animania:doe_fainting", CLUSTER, loot_list=default_loot)
# doe_havana = Creature("animania:doe_havana", CLUSTER, loot_list=default_loot)
# doe_jack = Creature("animania:doe_jack", CLUSTER, loot_list=default_loot)
# doe_kiko = Creature("animania:doe_kiko", CLUSTER, loot_list=default_loot)
# doe_kinder = Creature("animania:doe_kinder", CLUSTER, loot_list=default_loot)
# doe_lop = Creature("animania:doe_lop", CLUSTER, loot_list=default_loot)
# doe_new_zealand = Creature("animania:doe_new_zealand", CLUSTER, loot_list=default_loot)
# doe_nigerian_dwarf = Creature("animania:doe_nigerian_dwarf", CLUSTER, loot_list=default_loot)
# doe_pygmy = Creature("animania:doe_pygmy", CLUSTER, loot_list=default_loot)
# doe_rex = Creature("animania:doe_rex", CLUSTER, loot_list=default_loot)
# donkey = Creature("horse_colors:donkey", CLUSTER, loot_list=default_loot)
# eel_freshwater = Creature("betteranimalsplus:eel_freshwater", CLUSTER, loot_list=default_loot)
# eel_saltwater = Creature("betteranimalsplus:eel_saltwater", CLUSTER, loot_list=default_loot)
# enderman = Creature("minecraft:enderman", CLUSTER, loot_list=default_loot)
# evocation_illager = Creature("minecraft:evocation_illager", CLUSTER, loot_list=default_loot)
# ewe_dorper = Creature("animania:ewe_dorper", CLUSTER, loot_list=default_loot)
# ewe_dorset = Creature("animania:ewe_dorset", CLUSTER, loot_list=default_loot)
# ewe_friesian = Creature("animania:ewe_friesian", CLUSTER, loot_list=default_loot)
# ewe_jacob = Creature("animania:ewe_jacob", CLUSTER, loot_list=default_loot)
# ewe_merino = Creature("animania:ewe_merino", CLUSTER, loot_list=default_loot)
# ewe_suffolk = Creature("animania:ewe_suffolk", CLUSTER, loot_list=default_loot)
# feralwolf = Creature("betteranimalsplus:feralwolf", CLUSTER, loot_list=default_loot)
# ferret_grey = Creature("animania:ferret_grey", CLUSTER, loot_list=default_loot)
# ferret_white = Creature("animania:ferret_white", CLUSTER, loot_list=default_loot)
# foal_draft = Creature("animania:foal_draft", CLUSTER, loot_list=default_loot)
# foliaath = Creature("mowziesmobs:foliaath", CLUSTER, loot_list=default_loot)
# foliaath_baby = Creature("mowziesmobs:baby_foliaath", CLUSTER, loot_list=default_loot)
# fox = Creature("betteranimalsplus:fox", CLUSTER, loot_list=default_loot)
# frog = Creature("animania:frog", CLUSTER, loot_list=default_loot)
# frostmaw = Creature("mowziesmobs:frostmaw", CLUSTER, loot_list=default_loot)
# ghast = Creature("minecraft:ghast", CLUSTER, loot_list=default_loot)
# goose = Creature("betteranimalsplus:goose", CLUSTER, loot_list=default_loot)
# grottol = Creature("mowziesmobs:grottol", CLUSTER, loot_list=default_loot)
# hamster = Creature("animania:hamster", CLUSTER, loot_list=default_loot)
# hedgehog = Creature("animania:hedgehog", CLUSTER, loot_list=default_loot)
# hedgehog_albino = Creature("animania:hedgehog_albino", CLUSTER, loot_list=default_loot)
# hen_leghorn = Creature("animania:hen_leghorn", CLUSTER, loot_list=default_loot)
# hen_orpington = Creature("animania:hen_orpington", CLUSTER, loot_list=default_loot)
# hen_plymouth_rock = Creature("animania:hen_plymouth_rock", CLUSTER, loot_list=default_loot)
# hen_rhode_island_red = Creature("animania:hen_rhode_island_red", CLUSTER, loot_list=default_loot)
# hen_wyandotte = Creature("animania:hen_wyandotte", CLUSTER, loot_list=default_loot)
# hirschgeist = Creature("betteranimalsplus:hirschgeist", CLUSTER, loot_list=default_loot)
# hog_duroc = Creature("animania:hog_duroc", CLUSTER, loot_list=default_loot)
# hog_hampshire = Creature("animania:hog_hampshire", CLUSTER, loot_list=default_loot)
# hog_large_black = Creature("animania:hog_large_black", CLUSTER, loot_list=default_loot)
# hog_large_white = Creature("animania:hog_large_white", CLUSTER, loot_list=default_loot)
# hog_old_spot = Creature("animania:hog_old_spot", CLUSTER, loot_list=default_loot)
# hog_yorkshire = Creature("animania:hog_yorkshire", CLUSTER, loot_list=default_loot)
# horse = Creature("horse_colors:horse_felinoid", CLUSTER, loot_list=default_loot)
# horseshoecrab = Creature("betteranimalsplus:horseshoecrab", CLUSTER, loot_list=default_loot)
# husk = Creature("minecraft:husk", CLUSTER, loot_list=default_loot)
# illusion_illager = Creature("minecraft:illusion_illager", CLUSTER, loot_list=default_loot)
# jellyfish = Creature("betteranimalsplus:jellyfish", CLUSTER, loot_list=default_loot)
# kid_alpine = Creature("animania:kid_alpine", CLUSTER, loot_list=default_loot)
# kid_angora = Creature("animania:kid_angora", CLUSTER, loot_list=default_loot)
# kid_fainting = Creature("animania:kid_fainting", CLUSTER, loot_list=default_loot)
# kid_kiko = Creature("animania:kid_kiko", CLUSTER, loot_list=default_loot)
# kid_kinder = Creature("animania:kid_kinder", CLUSTER, loot_list=default_loot)
# kid_nigerian_dwarf = Creature("animania:kid_nigerian_dwarf", CLUSTER, loot_list=default_loot)
# kid_pygmy = Creature("animania:kid_pygmy", CLUSTER, loot_list=default_loot)
# kit_chinchilla = Creature("animania:kit_chinchilla", CLUSTER, loot_list=default_loot)
# kit_cottontail = Creature("animania:kit_cottontail", CLUSTER, loot_list=default_loot)
# kit_dutch = Creature("animania:kit_dutch", CLUSTER, loot_list=default_loot)
# kit_havana = Creature("animania:kit_havana", CLUSTER, loot_list=default_loot)
# kit_jack = Creature("animania:kit_jack", CLUSTER, loot_list=default_loot)
# kit_lop = Creature("animania:kit_lop", CLUSTER, loot_list=default_loot)
# kit_new_zealand = Creature("animania:kit_new_zealand", CLUSTER, loot_list=default_loot)
# kit_rex = Creature("animania:kit_rex", CLUSTER, loot_list=default_loot)
# lamb_dorper = Creature("animania:lamb_dorper", CLUSTER, loot_list=default_loot)
# lamb_dorset = Creature("animania:lamb_dorset", CLUSTER, loot_list=default_loot)
# lamb_friesian = Creature("animania:lamb_friesian", CLUSTER, loot_list=default_loot)
# lamb_jacob = Creature("animania:lamb_jacob", CLUSTER, loot_list=default_loot)
# lamb_merino = Creature("animania:lamb_merino", CLUSTER, loot_list=default_loot)
# lamb_suffolk = Creature("animania:lamb_suffolk", CLUSTER, loot_list=default_loot)
# lammergeier = Creature("betteranimalsplus:lammergeier", CLUSTER, loot_list=default_loot)
# lamprey = Creature("betteranimalsplus:lamprey", CLUSTER, loot_list=default_loot)
# lantern = Creature("mowziesmobs:lantern", CLUSTER, loot_list=default_loot)
# llama = Creature("minecraft:llama", CLUSTER, loot_list=default_loot)
# magma_cube = Creature("minecraft:magma_cube", CLUSTER, loot_list=default_loot)
# mare_draft = Creature("animania:mare_draft", CLUSTER, loot_list=default_loot)
# moose = Creature("betteranimalsplus:moose", CLUSTER, loot_list=default_loot)
# mooshroom = Creature("minecraft:mooshroom", CLUSTER, loot_list=default_loot)
# mule = Creature("horse_colors:mule", CLUSTER, loot_list=default_loot)
# naga = Creature("mowziesmobs:naga", CLUSTER, loot_list=default_loot)
# nautilus = Creature("betteranimalsplus:nautilus", CLUSTER, loot_list=default_loot)
# ocelot = Creature("minecraft:ocelot", CLUSTER, loot_list=default_loot)
# parrot = Creature("minecraft:parrot", CLUSTER, loot_list=default_loot)
# peachick_blue = Creature("animania:peachick_blue", CLUSTER, loot_list=default_loot)
# peachick_charcoal = Creature("animania:peachick_charcoal", CLUSTER, loot_list=default_loot)
# peachick_opal = Creature("animania:peachick_opal", CLUSTER, loot_list=default_loot)
# peachick_peach = Creature("animania:peachick_peach", CLUSTER, loot_list=default_loot)
# peachick_purple = Creature("animania:peachick_purple", CLUSTER, loot_list=default_loot)
# peachick_taupe = Creature("animania:peachick_taupe", CLUSTER, loot_list=default_loot)
# peachick_white = Creature("animania:peachick_white", CLUSTER, loot_list=default_loot)
# peacock_blue = Creature("animania:peacock_blue", CLUSTER, loot_list=default_loot)
# peacock_charcoal = Creature("animania:peacock_charcoal", CLUSTER, loot_list=default_loot)
# peacock_opal = Creature("animania:peacock_opal", CLUSTER, loot_list=default_loot)
# peacock_peach = Creature("animania:peacock_peach", CLUSTER, loot_list=default_loot)
# peacock_purple = Creature("animania:peacock_purple", CLUSTER, loot_list=default_loot)
# peacock_taupe = Creature("animania:peacock_taupe", CLUSTER, loot_list=default_loot)
# peacock_white = Creature("animania:peacock_white", CLUSTER, loot_list=default_loot)
# peahen_blue = Creature("animania:peahen_blue", CLUSTER, loot_list=default_loot)
# peahen_charcoal = Creature("animania:peahen_charcoal", CLUSTER, loot_list=default_loot)
# peahen_opal = Creature("animania:peahen_opal", CLUSTER, loot_list=default_loot)
# peahen_peach = Creature("animania:peahen_peach", CLUSTER, loot_list=default_loot)
# peahen_purple = Creature("animania:peahen_purple", CLUSTER, loot_list=default_loot)
# peahen_taupe = Creature("animania:peahen_taupe", CLUSTER, loot_list=default_loot)
# peahen_white = Creature("animania:peahen_white", CLUSTER, loot_list=default_loot)
# pheasant = Creature("betteranimalsplus:pheasant", CLUSTER, loot_list=default_loot)
# pig = Creature("minecraft:pig", CLUSTER, loot_list=default_loot)
# piglet_duroc = Creature("animania:piglet_duroc", CLUSTER, loot_list=default_loot)
# piglet_hampshire = Creature("animania:piglet_hampshire", CLUSTER, loot_list=default_loot)
# piglet_large_black = Creature("animania:piglet_large_black", CLUSTER, loot_list=default_loot)
# piglet_large_white = Creature("animania:piglet_large_white", CLUSTER, loot_list=default_loot)
# piglet_old_spot = Creature("animania:piglet_old_spot", CLUSTER, loot_list=default_loot)
# piglet_yorkshire = Creature("animania:piglet_yorkshire", CLUSTER, loot_list=default_loot)
# polar_bear = Creature("minecraft:polar_bear", CLUSTER, loot_list=default_loot)
# rabbit = Creature("minecraft:rabbit", CLUSTER, loot_list=default_loot)
# ram_dorper = Creature("animania:ram_dorper", CLUSTER, loot_list=default_loot)
# ram_dorset = Creature("animania:ram_dorset", CLUSTER, loot_list=default_loot)
# ram_friesian = Creature("animania:ram_friesian", CLUSTER, loot_list=default_loot)
# ram_jacob = Creature("animania:ram_jacob", CLUSTER, loot_list=default_loot)
# ram_merino = Creature("animania:ram_merino", CLUSTER, loot_list=default_loot)
# ram_suffolk = Creature("animania:ram_suffolk", CLUSTER, loot_list=default_loot)
# reindeer = Creature("betteranimalsplus:reindeer", CLUSTER, loot_list=default_loot)
# rooster_leghorn = Creature("animania:rooster_leghorn", CLUSTER, loot_list=default_loot)
# rooster_orpington = Creature("animania:rooster_orpington", CLUSTER, loot_list=default_loot)
# rooster_plymouth_rock = Creature("animania:rooster_plymouth_rock", CLUSTER, loot_list=default_loot)
# rooster_rhode_island_red = Creature("animania:rooster_rhode_island_red", CLUSTER, loot_list=default_loot)
# rooster_wyandotte = Creature("animania:rooster_wyandotte", CLUSTER, loot_list=default_loot)
# shark = Creature("betteranimalsplus:shark", CLUSTER, loot_list=default_loot)
# sheep = Creature("minecraft:sheep", CLUSTER, loot_list=default_loot)
# shulker = Creature("minecraft:shulker", CLUSTER, loot_list=default_loot)
# silverfish = Creature("minecraft:silverfish", CLUSTER, loot_list=default_loot)
# skeleton = Creature("minecraft:skeleton", CLUSTER, loot_list=default_loot)
# skeleton_horse = Creature("minecraft:skeleton_horse", CLUSTER, loot_list=default_loot)
# slime = Creature("minecraft:slime", CLUSTER, loot_list=default_loot)
# snowman = Creature("minecraft:snowman", CLUSTER, loot_list=default_loot)
# songbird = Creature("betteranimalsplus:songbird", CLUSTER, loot_list=default_loot)
# sow_duroc = Creature("animania:sow_duroc", CLUSTER, loot_list=default_loot)
# sow_hampshire = Creature("animania:sow_hampshire", CLUSTER, loot_list=default_loot)
# sow_large_black = Creature("animania:sow_large_black", CLUSTER, loot_list=default_loot)
# sow_large_white = Creature("animania:sow_large_white", CLUSTER, loot_list=default_loot)
# sow_old_spot = Creature("animania:sow_old_spot", CLUSTER, loot_list=default_loot)
# sow_yorkshire = Creature("animania:sow_yorkshire", CLUSTER, loot_list=default_loot)
# spider = Creature("minecraft:spider", CLUSTER, loot_list=default_loot)
# squid = Creature("minecraft:squid", CLUSTER, loot_list=default_loot)
# squirrel = Creature("betteranimalsplus:squirrel", CLUSTER, loot_list=default_loot)
# stallion_draft = Creature("animania:stallion_draft", CLUSTER, loot_list=default_loot)
# stray = Creature("minecraft:stray", CLUSTER, loot_list=default_loot)
# tarantula = Creature("betteranimalsplus:tarantula", CLUSTER, loot_list=default_loot)
# toad = Creature("animania:toad", CLUSTER, loot_list=default_loot)
# turkey = Creature("betteranimalsplus:turkey", CLUSTER, loot_list=default_loot)
# vex = Creature("minecraft:vex", CLUSTER, loot_list=default_loot)
# villager = Creature("minecraft:villager", CLUSTER, loot_list=default_loot)
# villager_golem = Creature("minecraft:villager_golem", CLUSTER, loot_list=default_loot)
# vindication_illager = Creature("minecraft:vindication_illager", CLUSTER, loot_list=default_loot)
# walrus = Creature("betteranimalsplus:walrus", CLUSTER, loot_list=default_loot)
# whale = Creature("betteranimalsplus:whale", CLUSTER, loot_list=default_loot)
# witch = Creature("minecraft:witch", CLUSTER, loot_list=default_loot)
# wither = Creature("minecraft:wither", CLUSTER, loot_list=default_loot)
# wither_skeleton = Creature("minecraft:wither_skeleton", CLUSTER, loot_list=default_loot)
# wolf = Creature("minecraft:wolf", CLUSTER, loot_list=default_loot)
# zombie = Creature("minecraft:zombie", CLUSTER, loot_list=default_loot)
# zombie_horse = Creature("minecraft:zombie_horse", CLUSTER, loot_list=default_loot)
# zombie_pigman = Creature("minecraft:zombie_pigman", CLUSTER, loot_list=default_loot)
# zombie_villager = Creature("minecraft:zombie_villager", CLUSTER, loot_list=default_loot)
# zotzpyre = Creature("betteranimalsplus:zotzpyre", CLUSTER, loot_list=default_loot)
