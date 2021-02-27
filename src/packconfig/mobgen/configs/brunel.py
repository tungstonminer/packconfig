"""Define the entity generation settings for Brunel 3."""

from packconfig import Range
from packconfig.mobgen import BiomeSet, ConfigFileSet, Loot, SpawnBuilder, Creature, Location
from packconfig.oregen import Ore, OreList
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
forest_hills = BiomeSet("Birch Forest Hills", "Birch Forest Hills M", "ForestHills", blocks=CARPETED)
forest_ice = BiomeSet("Ice Plains Spikes", blocks=SNOWY)
forest_temperate = BiomeSet("Birch Forest", "Birch Forest M", "Flower Forest", "Forest", blocks=CARPETED)
forest_jungle = BiomeSet("Jungle", "Jungle M", "JungleEdge", "JungleEdge M", "JungleHills", blocks=CARPETED)
mesa = BiomeSet(
    "Mesa", "Mesa (Bryce)", "Mesa Plateau", "Mesa Plateau F", "Mesa Plateau F M", "Mesa Plateau M",
    blocks=OreList(mc.red_sand, mc.red_sandstone, mc.dirt, mc.grass)
)
mountain = BiomeSet("Extreme Hills", "Extreme Hills M", "Extreme Hills Edge", blocks=GRASSY)
mountain_forest = BiomeSet("Extreme Hills+", "Extreme Hills+ M", blocks=GRASSY)
mushroom = BiomeSet("MushroomIsland", "MushroomIslandShore", blocks=FUNGAL)
nether = BiomeSet("Hell", blocks=HELLISH)
ocean = BiomeSet("Ocean", blocks=AQUATIC)
ocean_deep = BiomeSet("Deep Ocean", blocks=AQUATIC)
ocean_frozen = BiomeSet("FrozenOcean", blocks=AQUATIC)
plains = BiomeSet("Plains", "Sunflower Plains", blocks=GRASSY)
river = BiomeSet("River", blocks=OreList(mc.grass, mc.sand))
river_frozen = BiomeSet("FrozenRiver", blocks=OreList.merge(SNOWY, GRASSY))
savanna = BiomeSet("Savanna", "Savanna M", "Savanna Plateau", "Savanna Plateau M", blocks=GRASSY)
swamp = BiomeSet("DeepSwamp", "Marsh", "Swampland", "Swampland M", blocks=SWAMPY)
taiga = BiomeSet("Mega Spruce Taiga", "Mega Taiga", "Taiga", "Taiga M", blocks=CARPETED)
taiga_hills = BiomeSet("Mega Taiga Hills", "Redwood Taiga Hills M", "TaigaHills", blocks=CARPETED)
taiga_snowy = BiomeSet("Cold Taiga", "Cold Taiga M", "Cold Taiga Hills", blocks=CARPETED)
the_end = BiomeSet("The End", blocks=mc.endstone)
tundra = BiomeSet("CrystalChasms", "Ice Plains", "Ice Mountains", blocks=SNOWY)

earth = BiomeSet.merge(
    beach_cold, beach_sandy, beach_gravel, desert, forest_canopy, forest_hills, forest_ice, forest_temperate,
    forest_jungle, mesa, mountain, mountain_forest, mushroom, ocean, ocean_deep, ocean_frozen, plains, river,
    river_frozen, savanna, swamp, taiga, taiga_hills, taiga_snowy, tundra
)
settled = BiomeSet.merge(
    beach_sandy, desert, forest_canopy, forest_temperate, plains, river, savanna, taiga, taiga_snowy, swamp
)


# Loot Items  ##########################################################################################################

antler = "betteranimalsplus:antler"
bearhead_brown = "betteranimalsplus:bearhead_1"
bearhead_black = "betteranimalsplus:bearhead_2"
bearhead_polar = "betteranimalsplus:bearhead_3"
blaze_powder = "minecraft:blaze_powder"
blaze_rod = "minecraft:blaze_rod"
bone = "minecraft:bone"
bone_meal = "minecraft:dye:15"
bottle_o_enchanting = "minecraft:experience_bottle"
carcass_chicken = "minecraft:chicken"
carcass_chicken_prime = "animania:raw_prime_chicken"
carcass_clownfish = "minecraft:fish:2"
carcass_crab1 = "betteranimalsplus:crab_meat_raw"
carcass_crab2 = "harvestcraft:crabrawitem"
carcass_eel1 = "betteranimalsplus:eel_meat_raw"
carcass_eel2 = "harvestcraft:eelrawitem"
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
hirschgeist_skull = "betteranimalsplus:hirschgeistskull_1"
fur_black = "betteranimalsplus:bear_skin_black"
fur_brown = "betteranimalsplus:bear_skin_brown"
fur_white = "betteranimalsplus:bear_skin_kermode"
ink_sac = "minecraft:dye"
iron_block = "minecraft:iron_block"
iron_ingot = "minecraft:iron_ingot"
iron_nugget = "minecraft:iron_nugget"
kale = "harvestcraft:kaleitem"
luminous_jelly = "mowziesmobs:glowing_jelly"
magma_cream = "minecraft:magma_cream"
meat_bacon = "animania:raw_prime_bacon"
meat_beef = "minecraft:beef"
meat_beef_prime = "animania:raw_prime_beef"
meat_bird = "harvestcraft:groundchickenitem"
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
# meat_venison = "betteranimalsplus:venisonraw"
meat_venison = "harvestcraft:venisonrawitem"
mushroom_item = "minecraft:red_mushroom"
naga_fang = "mowziesmobs:naga_fang"
prismarine_shard = "minecraft:prismarine_shard"
rabbit_foot = "minecraft:rabbit_foot"
slime_ball = "minecraft:slime_ball"
snowball = "minecraft:snowball"
spider_eye = "minecraft:spider_eye"
turkey_meat = "harvestcraft:turkeyrawitem"
turtle_carcass = "harvestcraft:turtlerawitem"
wool = "minecraft:wool"


# Loot Lists ###########################################################################################################

default_loot = None
no_loot = []

bear_black_loot = [Loot("1-2", meat_beef), Loot("1-2", fur_black), Loot("1-2", bone), Loot("0-1", bearhead_brown)]
bear_brown_loot = [Loot("1-2", meat_beef), Loot("1-2", fur_brown), Loot("1-2", bone), Loot("0-1", bearhead_black)]
bear_polar_loot = [Loot("1-2", meat_beef), Loot("1-2", fur_white), Loot("1-2", bone), Loot("0-1", bearhead_polar)]
bird_raptor_loot = default_loot
bird_tiny_loot = default_loot
blaze_loot = [Loot("1-3", blaze_rod), Loot("1-3", blaze_powder)]
boar_loot = [Loot("2-4", meat_pork), Loot("1-2", hide_large)]
bovine_bull_loot = [Loot("1-2", meat_beef_prime), Loot("2-3", hide_large), Loot("2-3", bone)]
bovine_cow_loot = [Loot("1-2", meat_beef), Loot("1-2", hide_large), Loot("1-2", bone)]
bovine_calf_loot = [Loot("0-1", meat_beef), Loot("1-2", hide_small), Loot("1", bone)]
bovine_bull_mooshroom_loot = [Loot("1-2", meat_beef_prime), Loot("1-2", hide_large), Loot("2-3", mushroom_item)]
bovine_cow_mooshroom_loot = [Loot("1-2", meat_beef), Loot("0-1", hide_large), Loot("1-2", mushroom_item)]
bovine_calf_mooshroom_loot = [Loot("0-1", meat_beef), Loot("0-1", hide_small), Loot("0-1", mushroom_item)]
chicken_rooster_loot = [Loot("1-2", carcass_chicken_prime), Loot("1-2", feather_chicken_white), Loot("0-1", bone)]
chicken_hen_loot = [Loot("1-2", carcass_chicken), Loot("0-1", feather_chicken_white), Loot("0-1", bone)]
chicken_chick_loot = default_loot
coyote_loot = default_loot
crab_loot = [Loot("1-2", carcass_crab2), Loot("0-1", bone_meal)]
creeper_loot = [Loot("2-4", gunpowder)]
deer_loot = default_loot
donkey_loot = [Loot("1", hide_large), Loot("1", bone)]
eel_freshwater_loot = [Loot("1-2", carcass_eel1)]
eel_saltwater_loot = [Loot("1-2", carcass_eel2)]
enderman_loot = [Loot("1-2", ender_pearl)]
equine_loot = default_loot
evocation_illager_loot = default_loot
feralwolf_loot = default_loot
ferret_loot = [Loot("1", hide_small)]
fish_small_loot = default_loot
fish_large_loot = default_loot
foliaath_loot = default_loot
foliaath_baby_loot = default_loot
fox_loot = [Loot("1", hide_small)]
frog_loot = [Loot("1", meat_frog)]
frostmaw_loot = default_loot
ghast_loot = default_loot
goat_buck_loot = [Loot("1-2", meat_chevon_prime), Loot("1-2", hide_small)]
goat_doe_loot = [Loot("1-2", meat_chevon), Loot("1", hide_small)]
goat_kid_loot = [Loot("0-1", hide_small)]
goose_loot = default_loot
grottol_loot = default_loot
hamster_loot = default_loot
hedgehog_loot = default_loot
hirschgeist_loot = [Loot("1", hirschgeist_skull), Loot("2-3", bone)]
husk_loot = default_loot
horse_loot = [Loot("1", meat_horse), Loot("0-1", bone)]
horse_stallion_loot = [Loot("2-3", meat_horse), Loot("1-2", bone)]
horse_mare_loot = [Loot("1-2", meat_horse), Loot("0-1", bone)]
horse_foal_loot = default_loot
horseshoecrab_loot = [Loot("1-2", carcass_crab1), Loot("0-1", bone_meal)]
illusion_illager_loot = default_loot
jellyfish_loot = default_loot
lammergeier_loot = default_loot
lamprey_loot = default_loot
lantern_loot = default_loot
large_fish_loot = default_loot
llama_loot = [Loot("1-2", wool), Loot("1-2", bone)]
magma_cube_loot = default_loot
mammal_huge_loot = default_loot
mammal_medium_loot = default_loot
mammal_small_loot = [Loot("1", meat_chevon)]
moose_loot = default_loot
mule_loot = [Loot("1-2", hide_large), Loot("1-2", meat_horse), Loot("1-2", bone)]
naga_loot = default_loot
nautilus_loot = default_loot
ocelot_loot = default_loot
octopus_loot = [Loot("1-2", carcass_octopus), Loot("0-2", ink_sac)]
parrot_loot = default_loot
peafowl_blue_chick_loot = default_loot
peafowl_blue_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_blue_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_blue)]
peafowl_charcoal_chick_loot = default_loot
peafowl_charcoal_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_charcoal_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_charcoal)]
peafowl_opal_chick_loot = default_loot
peafowl_opal_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_opal_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_opal)]
peafowl_peach_chick_loot = default_loot
peafowl_peach_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_peach_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_peach)]
peafowl_purple_chick_loot = default_loot
peafowl_purple_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_purple_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_purple)]
peafowl_taupe_chick_loot = default_loot
peafowl_taupe_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_taupe_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_taupe)]
peafowl_white_chick_loot = default_loot
peafowl_white_hen_loot = [Loot("1-2", carcass_peacock)]
peafowl_white_cock_loot = [Loot("1-2", carcass_peacock_prime), Loot("1-2", feather_peacock_white)]
pheasant_loot = [Loot("1-2", carcass_pheasant)]
porcine_hog_loot = [Loot("1-2", meat_pork_prime), Loot("0-1", meat_bacon)]
porcine_sow_loot = [Loot("1-2", meat_pork)]
porcine_piglet_loot = default_loot
rabbit_buck_loot = [Loot("1", carcass_rabbit_prime), Loot("1-2", rabbit_foot), Loot("1-2", hide_small)]
rabbit_doe_loot = [Loot("1", carcass_rabbit), Loot("0-1", rabbit_foot), Loot("0-1", hide_small)]
rabbit_kit_loot = default_loot
reindeer_loot = [Loot("1-2", meat_venison), Loot("0-2", antler)]
shark_loot = default_loot
sheep_ewe_loot = [Loot("1-2", meat_mutton), Loot("1-2", wool)]
sheep_lamb_loot = default_loot
sheep_ram_loot = [Loot("1-2", meat_mutton_prime), Loot("1-3", wool)]
shulker_loot = default_loot
silverfish_loot = default_loot
skeleton_loot = default_loot
skeleton_horse_loot = default_loot
slime_loot = default_loot
snowman_loot = [Loot("8-12", snowball)]
spider_loot = [Loot("1-4", spider_eye)]
squid_loot = [Loot("1", carcass_squid), Loot("1-2", ink_sac)]
squirrel_loot = default_loot
stray_loot = default_loot
turkey_loot = [Loot("1", turkey_meat), Loot("1-2", meat_turkey_leg), Loot("1-2", feather_chicken_white)]
vex_loot = default_loot
villager_loot = default_loot
villager_golem_loot = default_loot
vindication_illager_loot = default_loot
walrus_loot = default_loot
whale_loot = default_loot
witch_loot = default_loot
wither_loot = default_loot
wither_skeleton_loot = default_loot
wolf_loot = default_loot
zombie_loot = default_loot
zombie_horse_loot = default_loot
zombie_pigman_loot = default_loot
zombie_villager_loot = default_loot
zotzpyre_loot = default_loot

# Entities #############################################################################################################

badger = Creature("betteranimalsplus:badger", LONER, loot_list=mammal_small_loot)
bat = Creature("minecraft:bat", HERD, loot_list=no_loot)
blackbear = Creature("betteranimalsplus:blackbear", PAIR, loot_list=bear_black_loot)
blaze = Creature("minecraft:blaze", CLUSTER, loot_list=blaze_loot)
boar = Creature("betteranimalsplus:boar", TROOP, loot_list=boar_loot)
bobbit_worm = Creature("betteranimalsplus:bobbit_worm", LONER, loot_list=no_loot)
brownbear = Creature("betteranimalsplus:brownbear", PAIR, loot_list=bear_brown_loot)
buck_alpine = Creature("animania:buck_alpine", TROOP, loot_list=goat_buck_loot)  # goat
buck_angora = Creature("animania:buck_angora", TROOP, loot_list=goat_buck_loot)  # goat
buck_chinchilla = Creature("animania:buck_chinchilla", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_cottontail = Creature("animania:buck_cottontail", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_dutch = Creature("animania:buck_dutch", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_fainting = Creature("animania:buck_fainting", TROOP, loot_list=goat_buck_loot)  # goat
buck_havana = Creature("animania:buck_havana", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_jack = Creature("animania:buck_jack", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_kiko = Creature("animania:buck_kiko", TROOP, loot_list=goat_buck_loot)  # goat
buck_kinder = Creature("animania:buck_kinder", TROOP, loot_list=goat_buck_loot)  # goat
buck_lop = Creature("animania:buck_lop", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_new_zealand = Creature("animania:buck_new_zealand", HERD, loot_list=rabbit_buck_loot)  # rabbit
buck_nigerian_dwarf = Creature("animania:buck_nigerian_dwarf", TROOP, loot_list=goat_buck_loot)  # goat
buck_pygmy = Creature("animania:buck_pygmy", TROOP, loot_list=goat_buck_loot)  # goat
buck_rex = Creature("animania:buck_rex", HERD, loot_list=rabbit_buck_loot)  # rabbit
bull_angus = Creature("animania:bull_angus", CLUSTER, loot_list=bovine_bull_loot)
bull_friesian = Creature("animania:bull_friesian", CLUSTER, loot_list=bovine_bull_loot)
bull_hereford = Creature("animania:bull_hereford", CLUSTER, loot_list=bovine_bull_loot)
bull_highland = Creature("animania:bull_highland", CLUSTER, loot_list=bovine_bull_loot)
bull_holstein = Creature("animania:bull_holstein", CLUSTER, loot_list=bovine_bull_loot)
bull_jersey = Creature("animania:bull_jersey", CLUSTER, loot_list=bovine_bull_loot)
bull_longhorn = Creature("animania:bull_longhorn", CLUSTER, loot_list=bovine_bull_loot)
bull_mooshroom = Creature("animania:bull_mooshroom", CLUSTER, loot_list=bovine_bull_mooshroom_loot)
calf_angus = Creature("animania:calf_angus", CLUSTER, loot_list=bovine_calf_loot)
calf_friesian = Creature("animania:calf_friesian", CLUSTER, loot_list=bovine_calf_loot)
calf_hereford = Creature("animania:calf_hereford", CLUSTER, loot_list=bovine_calf_loot)
calf_highland = Creature("animania:calf_highland", CLUSTER, loot_list=bovine_calf_loot)
calf_holstein = Creature("animania:calf_holstein", CLUSTER, loot_list=bovine_calf_loot)
calf_jersey = Creature("animania:calf_jersey", CLUSTER, loot_list=bovine_calf_loot)
calf_longhorn = Creature("animania:calf_longhorn", CLUSTER, loot_list=bovine_calf_loot)
calf_mooshroom = Creature("animania:calf_mooshroom", CLUSTER, loot_list=bovine_calf_mooshroom_loot)
cave_spider = Creature("minecraft:cave_spider", PAIR, loot_list=spider_loot)
chick_leghorn = Creature("animania:chick_leghorn", TROOP, loot_list=chicken_chick_loot)
chick_orpington = Creature("animania:chick_orpington", TROOP, loot_list=chicken_chick_loot)
chick_plymouth_rock = Creature("animania:chick_plymouth_rock", TROOP, loot_list=chicken_chick_loot)
chick_rhode_island_red = Creature("animania:chick_rhode_island_red", TROOP, loot_list=chicken_chick_loot)
chick_wyandotte = Creature("animania:chick_wyandotte", TROOP, loot_list=chicken_chick_loot)
chicken = Creature("minecraft:chicken", LONER, loot_list=default_loot)
cow = Creature("minecraft:cow", LONER, loot_list=default_loot)
cow_angus = Creature("animania:cow_angus", CLUSTER, loot_list=bovine_cow_loot)
cow_friesian = Creature("animania:cow_friesian", CLUSTER, loot_list=bovine_cow_loot)
cow_hereford = Creature("animania:cow_hereford", CLUSTER, loot_list=bovine_cow_loot)
cow_highland = Creature("animania:cow_highland", CLUSTER, loot_list=bovine_cow_loot)
cow_holstein = Creature("animania:cow_holstein", CLUSTER, loot_list=bovine_cow_loot)
cow_jersey = Creature("animania:cow_jersey", CLUSTER, loot_list=bovine_cow_loot)
cow_longhorn = Creature("animania:cow_longhorn", CLUSTER, loot_list=bovine_cow_loot)
cow_mooshroom = Creature("animania:cow_mooshroom", CLUSTER, loot_list=bovine_calf_mooshroom_loot)
coyote = Creature("betteranimalsplus:coyote", CLUSTER, loot_list=coyote_loot)
crab = Creature("betteranimalsplus:crab", PAIR, loot_list=crab_loot)
creeper = Creature("minecraft:creeper", LONER, loot_list=creeper_loot)
dartfrog = Creature("animania:dartfrog", PAIR, loot_list=frog_loot)
deer = Creature("betteranimalsplus:deer", CLUSTER, loot_list=deer_loot)
doe_alpine = Creature("animania:doe_alpine", TROOP, loot_list=goat_doe_loot)  # goat
doe_angora = Creature("animania:doe_angora", TROOP, loot_list=goat_doe_loot)  # goat
doe_chinchilla = Creature("animania:doe_chinchilla", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_cottontail = Creature("animania:doe_cottontail", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_dutch = Creature("animania:doe_dutch", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_fainting = Creature("animania:doe_fainting", TROOP, loot_list=goat_doe_loot)  # goat
doe_havana = Creature("animania:doe_havana", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_jack = Creature("animania:doe_jack", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_kiko = Creature("animania:doe_kiko", TROOP, loot_list=goat_doe_loot)  # goat
doe_kinder = Creature("animania:doe_kinder", TROOP, loot_list=goat_doe_loot)  # goat
doe_lop = Creature("animania:doe_lop", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_new_zealand = Creature("animania:doe_new_zealand", HERD, loot_list=rabbit_doe_loot)  # rabbit
doe_nigerian_dwarf = Creature("animania:doe_nigerian_dwarf", TROOP, loot_list=goat_doe_loot)  # goat
doe_pygmy = Creature("animania:doe_pygmy", TROOP, loot_list=goat_doe_loot)  # goat
doe_rex = Creature("animania:doe_rex", HERD, loot_list=rabbit_doe_loot)  # rabbit
donkey = Creature("horse_colors:donkey", TROOP, loot_list=donkey_loot)
eel_freshwater = Creature("betteranimalsplus:eel_freshwater", CLUSTER, loot_list=eel_freshwater_loot)
eel_saltwater = Creature("betteranimalsplus:eel_saltwater", CLUSTER, loot_list=eel_saltwater_loot)
enderman = Creature("minecraft:enderman", LONER, loot_list=enderman_loot)
evocation_illager = Creature("minecraft:evocation_illager", CLUSTER, loot_list=evocation_illager_loot)
ewe_dorper = Creature("animania:ewe_dorper", HERD, loot_list=sheep_ewe_loot)
ewe_dorset = Creature("animania:ewe_dorset", HERD, loot_list=sheep_ewe_loot)
ewe_friesian = Creature("animania:ewe_friesian", HERD, loot_list=sheep_ewe_loot)
ewe_jacob = Creature("animania:ewe_jacob", HERD, loot_list=sheep_ewe_loot)
ewe_merino = Creature("animania:ewe_merino", HERD, loot_list=sheep_ewe_loot)
ewe_suffolk = Creature("animania:ewe_suffolk", HERD, loot_list=sheep_ewe_loot)
feralwolf = Creature("betteranimalsplus:feralwolf", CLUSTER, loot_list=feralwolf_loot)
ferret_grey = Creature("animania:ferret_grey", CLUSTER, loot_list=ferret_loot)
ferret_white = Creature("animania:ferret_white", CLUSTER, loot_list=ferret_loot)
foal_draft = Creature("animania:foal_draft", CLUSTER, loot_list=horse_foal_loot)
foliaath = Creature("mowziesmobs:foliaath", LONER, loot_list=foliaath_loot)
foliaath_baby = Creature("mowziesmobs:baby_foliaath", LONER, loot_list=foliaath_baby_loot)
fox = Creature("betteranimalsplus:fox", CLUSTER, loot_list=fox_loot)
frog = Creature("animania:frog", PAIR, loot_list=frog_loot)
frostmaw = Creature("mowziesmobs:frostmaw", LONER, loot_list=frostmaw_loot)
ghast = Creature("minecraft:ghast", LONER, loot_list=ghast_loot)
goose = Creature("betteranimalsplus:goose", CLUSTER, loot_list=goose_loot)
grottol = Creature("mowziesmobs:grottol", LONER, loot_list=grottol_loot)
hamster = Creature("animania:hamster", CLUSTER, loot_list=hamster_loot)
hedgehog = Creature("animania:hedgehog", CLUSTER, loot_list=hedgehog_loot)
hedgehog_albino = Creature("animania:hedgehog_albino", CLUSTER, loot_list=hedgehog_loot)
hen_leghorn = Creature("animania:hen_leghorn", TROOP, loot_list=chicken_hen_loot)
hen_orpington = Creature("animania:hen_orpington", TROOP, loot_list=chicken_hen_loot)
hen_plymouth_rock = Creature("animania:hen_plymouth_rock", TROOP, loot_list=chicken_hen_loot)
hen_rhode_island_red = Creature("animania:hen_rhode_island_red", TROOP, loot_list=chicken_hen_loot)
hen_wyandotte = Creature("animania:hen_wyandotte", TROOP, loot_list=chicken_hen_loot)
hirschgeist = Creature("betteranimalsplus:hirschgeist", LONER, loot_list=hirschgeist_loot)
hog_duroc = Creature("animania:hog_duroc", CLUSTER, loot_list=porcine_hog_loot)
hog_hampshire = Creature("animania:hog_hampshire", CLUSTER, loot_list=porcine_hog_loot)
hog_large_black = Creature("animania:hog_large_black", CLUSTER, loot_list=porcine_hog_loot)
hog_large_white = Creature("animania:hog_large_white", CLUSTER, loot_list=porcine_hog_loot)
hog_old_spot = Creature("animania:hog_old_spot", CLUSTER, loot_list=porcine_hog_loot)
hog_yorkshire = Creature("animania:hog_yorkshire", CLUSTER, loot_list=porcine_hog_loot)
horse = Creature("horse_colors:horse_felinoid", TROOP, loot_list=horse_loot)
horseshoecrab = Creature("betteranimalsplus:horseshoecrab", PAIR, loot_list=horseshoecrab_loot)
husk = Creature("minecraft:husk", LONER, loot_list=husk_loot)
illusion_illager = Creature("minecraft:illusion_illager", LONER, loot_list=illusion_illager_loot)
jellyfish = Creature("betteranimalsplus:jellyfish", SWARM, loot_list=jellyfish_loot)
kid_alpine = Creature("animania:kid_alpine", TROOP, loot_list=goat_kid_loot)  # goat
kid_angora = Creature("animania:kid_angora", TROOP, loot_list=goat_kid_loot)  # goat
kid_fainting = Creature("animania:kid_fainting", TROOP, loot_list=goat_kid_loot)  # goat
kid_kiko = Creature("animania:kid_kiko", TROOP, loot_list=goat_kid_loot)  # goat
kid_kinder = Creature("animania:kid_kinder", TROOP, loot_list=goat_kid_loot)  # goat
kid_nigerian_dwarf = Creature("animania:kid_nigerian_dwarf", TROOP, loot_list=goat_kid_loot)  # goat
kid_pygmy = Creature("animania:kid_pygmy", TROOP, loot_list=goat_kid_loot)  # goat
kit_chinchilla = Creature("animania:kit_chinchilla", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_cottontail = Creature("animania:kit_cottontail", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_dutch = Creature("animania:kit_dutch", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_havana = Creature("animania:kit_havana", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_jack = Creature("animania:kit_jack", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_lop = Creature("animania:kit_lop", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_new_zealand = Creature("animania:kit_new_zealand", HERD, loot_list=rabbit_kit_loot)  # rabbit
kit_rex = Creature("animania:kit_rex", HERD, loot_list=rabbit_kit_loot)  # rabbit
lamb_dorper = Creature("animania:lamb_dorper", HERD, loot_list=sheep_lamb_loot)
lamb_dorset = Creature("animania:lamb_dorset", HERD, loot_list=sheep_lamb_loot)
lamb_friesian = Creature("animania:lamb_friesian", HERD, loot_list=sheep_lamb_loot)
lamb_jacob = Creature("animania:lamb_jacob", HERD, loot_list=sheep_lamb_loot)
lamb_merino = Creature("animania:lamb_merino", HERD, loot_list=sheep_lamb_loot)
lamb_suffolk = Creature("animania:lamb_suffolk", HERD, loot_list=sheep_lamb_loot)
lammergeier = Creature("betteranimalsplus:lammergeier", CLUSTER, loot_list=lammergeier_loot)
lamprey = Creature("betteranimalsplus:lamprey", LONER, loot_list=lamprey_loot)
lantern = Creature("mowziesmobs:lantern", CLUSTER, loot_list=lantern_loot)
llama = Creature("minecraft:llama", CLUSTER, loot_list=llama_loot)
magma_cube = Creature("minecraft:magma_cube", LONER, loot_list=magma_cube_loot)
mare_draft = Creature("animania:mare_draft", TROOP, loot_list=horse_mare_loot)
moose = Creature("betteranimalsplus:moose", CLUSTER, loot_list=moose_loot)
mooshroom = Creature("minecraft:mooshroom", LONER, loot_list=default_loot)
mule = Creature("horse_colors:mule", CLUSTER, loot_list=mule_loot)
naga = Creature("mowziesmobs:naga", LONER, loot_list=naga_loot)
nautilus = Creature("betteranimalsplus:nautilus", PAIR, loot_list=nautilus_loot)
ocelot = Creature("minecraft:ocelot", PAIR, loot_list=ocelot_loot)
parrot = Creature("minecraft:parrot", PAIR, loot_list=default_loot)
peachick_blue = Creature("animania:peachick_blue", TROOP, loot_list=peafowl_blue_chick_loot)
peachick_charcoal = Creature("animania:peachick_charcoal", TROOP, loot_list=peafowl_charcoal_chick_loot)
peachick_opal = Creature("animania:peachick_opal", TROOP, loot_list=peafowl_opal_chick_loot)
peachick_peach = Creature("animania:peachick_peach", TROOP, loot_list=peafowl_peach_chick_loot)
peachick_purple = Creature("animania:peachick_purple", TROOP, loot_list=peafowl_purple_chick_loot)
peachick_taupe = Creature("animania:peachick_taupe", TROOP, loot_list=peafowl_taupe_chick_loot)
peachick_white = Creature("animania:peachick_white", TROOP, loot_list=peafowl_white_chick_loot)
peacock_blue = Creature("animania:peacock_blue", TROOP, loot_list=peafowl_blue_cock_loot)
peacock_charcoal = Creature("animania:peacock_charcoal", TROOP, loot_list=peafowl_charcoal_cock_loot)
peacock_opal = Creature("animania:peacock_opal", TROOP, loot_list=peafowl_opal_cock_loot)
peacock_peach = Creature("animania:peacock_peach", TROOP, loot_list=peafowl_peach_cock_loot)
peacock_purple = Creature("animania:peacock_purple", TROOP, loot_list=peafowl_purple_cock_loot)
peacock_taupe = Creature("animania:peacock_taupe", TROOP, loot_list=peafowl_taupe_cock_loot)
peacock_white = Creature("animania:peacock_white", TROOP, loot_list=peafowl_white_cock_loot)
peahen_blue = Creature("animania:peahen_blue", TROOP, loot_list=peafowl_blue_hen_loot)
peahen_charcoal = Creature("animania:peahen_charcoal", TROOP, loot_list=peafowl_charcoal_hen_loot)
peahen_opal = Creature("animania:peahen_opal", TROOP, loot_list=peafowl_opal_hen_loot)
peahen_peach = Creature("animania:peahen_peach", TROOP, loot_list=peafowl_peach_hen_loot)
peahen_purple = Creature("animania:peahen_purple", TROOP, loot_list=peafowl_purple_hen_loot)
peahen_taupe = Creature("animania:peahen_taupe", TROOP, loot_list=peafowl_taupe_hen_loot)
peahen_white = Creature("animania:peahen_white", TROOP, loot_list=peafowl_white_hen_loot)
pheasant = Creature("betteranimalsplus:pheasant", TROOP, loot_list=pheasant_loot)
pig = Creature("minecraft:pig", LONER, loot_list=default_loot)
piglet_duroc = Creature("animania:piglet_duroc", CLUSTER, loot_list=porcine_piglet_loot)
piglet_hampshire = Creature("animania:piglet_hampshire", CLUSTER, loot_list=porcine_piglet_loot)
piglet_large_black = Creature("animania:piglet_large_black", CLUSTER, loot_list=porcine_piglet_loot)
piglet_large_white = Creature("animania:piglet_large_white", CLUSTER, loot_list=porcine_piglet_loot)
piglet_old_spot = Creature("animania:piglet_old_spot", CLUSTER, loot_list=porcine_piglet_loot)
piglet_yorkshire = Creature("animania:piglet_yorkshire", CLUSTER, loot_list=porcine_piglet_loot)
polar_bear = Creature("minecraft:polar_bear", LONER, loot_list=bear_polar_loot)
rabbit = Creature("minecraft:rabbit", LONER, loot_list=default_loot)
ram_dorper = Creature("animania:ram_dorper", HERD, loot_list=sheep_ram_loot)
ram_dorset = Creature("animania:ram_dorset", HERD, loot_list=sheep_ram_loot)
ram_friesian = Creature("animania:ram_friesian", HERD, loot_list=sheep_ram_loot)
ram_jacob = Creature("animania:ram_jacob", HERD, loot_list=sheep_ram_loot)
ram_merino = Creature("animania:ram_merino", HERD, loot_list=sheep_ram_loot)
ram_suffolk = Creature("animania:ram_suffolk", HERD, loot_list=sheep_ram_loot)
reindeer = Creature("betteranimalsplus:reindeer", CLUSTER, loot_list=reindeer_loot)
rooster_leghorn = Creature("animania:rooster_leghorn", CLUSTER, loot_list=chicken_rooster_loot)
rooster_orpington = Creature("animania:rooster_orpington", CLUSTER, loot_list=chicken_rooster_loot)
rooster_plymouth_rock = Creature("animania:rooster_plymouth_rock", CLUSTER, loot_list=chicken_rooster_loot)
rooster_rhode_island_red = Creature("animania:rooster_rhode_island_red", CLUSTER, loot_list=chicken_rooster_loot)
rooster_wyandotte = Creature("animania:rooster_wyandotte", CLUSTER, loot_list=chicken_rooster_loot)
shark = Creature("betteranimalsplus:shark", CLUSTER, loot_list=shark_loot)
sheep = Creature("minecraft:sheep", LONER, loot_list=default_loot)
shulker = Creature("minecraft:shulker", CLUSTER, loot_list=shulker_loot)
silverfish = Creature("minecraft:silverfish", CLUSTER, loot_list=silverfish_loot)
skeleton = Creature("minecraft:skeleton", CLUSTER, loot_list=skeleton_loot)
skeleton_horse = Creature("minecraft:skeleton_horse", CLUSTER, loot_list=skeleton_horse_loot)
slime = Creature("minecraft:slime", PAIR, loot_list=slime_loot)
snowman = Creature("minecraft:snowman", LONER, loot_list=snowman_loot)
songbird = Creature("betteranimalsplus:songbird", CLUSTER, loot_list=bird_tiny_loot)
sow_duroc = Creature("animania:sow_duroc", CLUSTER, loot_list=porcine_sow_loot)
sow_hampshire = Creature("animania:sow_hampshire", CLUSTER, loot_list=porcine_sow_loot)
sow_large_black = Creature("animania:sow_large_black", CLUSTER, loot_list=porcine_sow_loot)
sow_large_white = Creature("animania:sow_large_white", CLUSTER, loot_list=porcine_sow_loot)
sow_old_spot = Creature("animania:sow_old_spot", CLUSTER, loot_list=porcine_sow_loot)
sow_yorkshire = Creature("animania:sow_yorkshire", CLUSTER, loot_list=porcine_sow_loot)
spider = Creature("minecraft:spider", LONER, loot_list=spider_loot)
squid = Creature("minecraft:squid", TROOP, loot_list=squid_loot)
squirrel = Creature("betteranimalsplus:squirrel", CLUSTER, loot_list=squirrel_loot)
stallion_draft = Creature("animania:stallion_draft", TROOP, loot_list=horse_stallion_loot)
stray = Creature("minecraft:stray", CLUSTER, loot_list=stray_loot)
tarantula = Creature("betteranimalsplus:tarantula", LONER, loot_list=spider_loot)
toad = Creature("animania:toad", PAIR, loot_list=frog_loot)
turkey = Creature("betteranimalsplus:turkey", CLUSTER, loot_list=turkey_loot)
vex = Creature("minecraft:vex", LONER, loot_list=vex_loot)
villager = Creature("minecraft:villager", TROOP, loot_list=villager_loot)
villager_golem = Creature("minecraft:villager_golem", PAIR, loot_list=villager_golem_loot)
vindication_illager = Creature("minecraft:vindication_illager", LONER, loot_list=vindication_illager_loot)
walrus = Creature("betteranimalsplus:walrus", CLUSTER, loot_list=walrus_loot)
whale = Creature("betteranimalsplus:whale", CLUSTER, loot_list=whale_loot)
witch = Creature("minecraft:witch", LONER, loot_list=witch_loot)
wither = Creature("minecraft:wither", LONER, loot_list=wither_loot)
wither_skeleton = Creature("minecraft:wither_skeleton", LONER, loot_list=wither_skeleton_loot)
wolf = Creature("minecraft:wolf", PAIR, loot_list=wolf_loot)
zombie = Creature("minecraft:zombie", LONER, loot_list=zombie_loot)
zombie_horse = Creature("minecraft:zombie_horse", LONER, loot_list=zombie_horse_loot)
zombie_pigman = Creature("minecraft:zombie_pigman", LONER, loot_list=zombie_pigman_loot)
zombie_villager = Creature("minecraft:zombie_villager", LONER, loot_list=zombie_villager_loot)
zotzpyre = Creature("betteranimalsplus:zotzpyre", LONER, loot_list=zotzpyre_loot)

# Entity Spawn ####################################################################################################

b = SpawnBuilder()

with b.location(Location(beach_cold)):
    with b.active_periods(DAY):
        with b.spawn(20, 60):
            pass


with b.location(Location(beach_gravel)):
    with b.active_periods(DAY):
        with b.spawn(8, 90):
            b.add(walrus.configure(25, 3))


with b.location(Location(beach_sandy)):
    with b.active_periods(DAY):
        with b.spawn(10, 15):
            b.add(crab.configure(25, 3))
            b.add(horseshoecrab.configure(10, 3))


with b.location(Location(desert)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(hamster.configure(25, 5))
            b.add(doe_nigerian_dwarf.configure(5, 1))

    with b.active_periods(NIGHT):
        with b.spawn(3, 90):
            b.add(tarantula.configure(1, 3))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(doe_jack.configure(15, 3))

with b.location(Location(desert.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.light(upper=0):
                with b.spawn(16, 90):
                    b.add(blaze.configure(5, 10))


with b.location(Location(forest_canopy)):
    with b.active_periods(DAY):
        with b.spawn(40, 30):
            b.add(sow_large_black.configure(25, 5))
            b.add(ewe_friesian.configure(15, 4))
            b.add(cow_angus.configure(5, 3))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(doe_lop.configure(25, 3))


with b.location(Location(forest_hills)):
    with b.active_periods(DAY):
        with b.spawn(40, 90):
            b.add(pheasant.configure(40, 5))
            b.add(badger.configure(30, 2))
            b.add(hen_rhode_island_red.configure(20, 3))
            b.add(sow_large_white.configure(10, 3))
            b.add(cow_hereford.configure(5, 2))
            b.add(blackbear.configure(1, 1))

    with b.active_periods(NIGHT):
        with b.spawn(5, 90):
            b.add(fox.configure(10, 5))


with b.location(Location(forest_ice)):
    with b.active_periods(ANY):
        with b.spawn(1, 120):
            b.add(frostmaw.configure(1, 1))


with b.location(Location(forest_jungle)):
    with b.active_periods(DAY):
        with b.spawn(20, 30):
            b.add(parrot.configure(60, 5))
            b.add(hen_orpington.configure(40, 4))
            b.add(sow_duroc.configure(20, 4))
            b.add(peahen_opal.configure(2, 1))
            b.add(peahen_purple.configure(2, 1))
            b.add(peahen_blue.configure(2, 1))
            b.add(peahen_peach.configure(2, 1))

    with b.active_periods(NIGHT):
        with b.spawn(20, 30):
            b.add(dartfrog.configure(80, 10))
            b.add(ocelot.configure(5, 2))

    with b.active_periods(ANY):
        with b.spawn(4, 30):
            b.add(foliaath.configure(1, 4))


with b.location(Location(forest_temperate)):
    with b.active_periods(DAY):
        with b.spawn(40, 30):
            b.add(squirrel.configure(50, 5))
            b.add(songbird.configure(50, 5))
            b.add(deer.configure(25, 2))
            b.add(hen_wyandotte.configure(15, 4))
            b.add(ewe_jacob.configure(10, 3))
            b.add(cow_holstein.configure(5, 2))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(doe_cottontail.configure(25, 3))

    with b.active_periods(NIGHT):
        with b.spawn(5, 30):
            b.add(fox.configure(25, 3))


with b.location(Location(mesa)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(doe_pygmy.configure(30, 4))
            b.add(ewe_suffolk.configure(20, 4))
            b.add(donkey.configure(10, 2))

    with b.active_periods(NIGHT):
        with b.spawn(20, 60):
            b.add(coyote.configure(25, 3))


with b.location(Location(mesa.in_cave())):
    with b.active_periods(ANY):
        with b.light(upper=0):
            with b.spawn(16, 90):
                b.add(blaze.configure(5, 10))


with b.location(Location(mountain)):
    with b.active_periods(DAY):
        with b.altitude(lower=110):
            with b.spawn(15, 90):
                b.add(lammergeier.configure(40, 5))
                b.add(doe_alpine.configure(10, 5))
                b.add(naga.configure(1, 3))

        with b.altitude(upper=110):
            with b.spawn(10, 90):
                b.add(doe_chinchilla.configure(15, 5))
                b.add(llama.configure(5, 3))

    with b.active_periods(NIGHT):
        with b.altitude(upper=110):
            with b.spawn(20, 60):
                b.add(wolf.configure(25, 3))

with b.location(Location(mountain.in_cave())):
    with b.active_periods(ANY):
        with b.spawn(3, 90):
            b.add(villager_golem.configure(1, 2))


with b.location(Location(mountain_forest)):
    with b.active_periods(DAY):
        with b.spawn(30, 60):
            b.add(hen_plymouth_rock.configure(30, 5))
            b.add(doe_kiko.configure(15, 4))
            b.add(sow_hampshire.configure(10, 3))
            b.add(cow_highland.configure(5, 2))

    with b.active_periods(NIGHT):
        with b.spawn(10, 60):
            b.add(hedgehog.configure(40, 5))


with b.location(Location(mushroom)):
    with b.active_periods(ANY):
        with b.spawn(30, 30):
            b.add(cow_mooshroom.configure(100, 6))


with b.location(Location(ocean)):
    with b.active_periods(ANY):
        with b.spawn(40, 30):
            b.add(squid.configure(50, 5))
            b.add(jellyfish.configure(40, 5))
            b.add(eel_saltwater.configure(30, 4))
            b.add(bobbit_worm.configure(20, 3))
            b.add(shark.configure(10, 2))


with b.location(Location(ocean_deep)):
    with b.active_periods(ANY):
        with b.spawn(30, 60):
            b.add(jellyfish.configure(25, 3))
            b.add(nautilus.configure(20, 4))
            b.add(whale.configure(5, 2))


with b.location(Location(ocean_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(10, 90):
            b.add(whale.configure(5, 2))


with b.location(Location(nether)):
    with b.active_periods(ANY):
        with b.spawn(20, 15):
            b.add(skeleton.configure(20, 5))
            b.add(zombie.configure(10, 4))
            b.add(zombie_villager.configure(5, 3))


with b.location(Location(plains)):
    with b.active_periods(DAY):
        with b.spawn(20, 60):
            b.add(hen_leghorn.configure(50, 5))
            b.add(ewe_dorper.configure(40, 3))
            b.add(doe_angora.configure(30, 3))
            b.add(cow_friesian.configure(20, 3))
            b.add(mare_draft.configure(10, 2))

    with b.active_periods(NIGHT):
        with b.spawn(10, 60):
            b.add(ferret_grey.configure(50, 4))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(doe_dutch.configure(25, 4))


with b.location(Location(river.in_water())):
    with b.active_periods(ANY):
        with b.spawn(20, 60):
            b.add(eel_freshwater.configure(25, 5))


with b.location(Location(river_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(20, 60):
            pass


with b.location(Location(savanna)):
    with b.active_periods(DAY):
        with b.spawn(30, 60):
            b.add(toad.configure(40, 5))
            b.add(doe_kinder.configure(30, 4))
            b.add(ewe_merino.configure(30, 4))
            b.add(cow_longhorn.configure(20, 4))
            b.add(horse.configure(10, 3))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(doe_rex.configure(25, 3))


village_blocks = [Ore("minecraft:grass_path"), mc.dirt, mc.grass, mc.gravel, Ore("minecraft:log")]
with b.location(Location(settled.with_blocks(village_blocks), structure="Village")):
    with b.active_periods(DAY):
        with b.spawn(1, 90):
            b.add(villager_golem.configure(5, 1))


with b.location(Location(settled.in_cave().with_blocks(mc.cobblestone, mc.dirt, mc.planks), structure="Village")):
    with b.active_periods(NIGHT):
        with b.spawn(20, 60):
            b.add(villager.configure(1, 4))


with b.location(Location(swamp)):
    with b.active_periods(DAY):
        with b.spawn(40, 30):
            b.add(frog.configure(60, 10))
            b.add(goose.configure(40, 5))
            b.add(sow_yorkshire.configure(20, 4))
            b.add(peahen_taupe.configure(4, 2))
            b.add(peahen_charcoal.configure(3, 1))
            b.add(peahen_white.configure(3, 1))
            b.add(cow_jersey.configure(5, 2))

    with b.active_periods(NIGHT):
        with b.spawn(10, 60):
            b.add(slime.configure(25, 4))


with b.location(Location(swamp.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=24):
            with b.spawn(3, 90):
                b.add(grottol.configure(5, 3))


with b.location(Location(swamp.in_water())):
    with b.active_periods(ANY):
        with b.spawn(20, 15):
            b.add(eel_freshwater.configure(20, 5))
            b.add(lamprey.configure(10, 5))


with b.location(Location(swamp, weather="rain")):
    with b.active_periods(ANY):
        with b.spawn(10, 15):
            b.add(slime.configure(50, 5))


with b.location(Location(swamp, structure="Temple")):
    with b.active_periods(ANY):
        with b.spawn(1, 1):
            b.add(witch.configure(100, 1))


with b.location(Location(taiga)):
    with b.active_periods(DAY):
        with b.spawn(20, 90):
            b.add(doe_havana.configure(40, 5))
            b.add(turkey.configure(20, 3))
            b.add(brownbear.configure(5, 2))


with b.location(Location(taiga_hills)):
    with b.active_periods(DAY):
        with b.spawn(20, 60):
            b.add(ewe_dorset.configure(30, 4))
            b.add(moose.configure(10, 2))

    with b.active_periods(NIGHT):
        with b.spawn(5, 60):
            b.add(wolf.configure(25, 1))


with b.location(Location(taiga_snowy)):
    with b.active_periods(DAY):
        with b.spawn(20, 90):
            b.add(doe_fainting.configure(30, 4))
            b.add(reindeer.configure(20, 3))
            b.add(feralwolf.configure(5, 1))

    with b.active_periods(NIGHT):
        with b.spawn(1, 90):
            b.add(hirschgeist.configure(1, 3))


with b.location(Location(the_end)):
    with b.active_periods(ANY):
        with b.spawn(80, 15):
            b.add(enderman.configure(100, 20, Range(1, 4)))


with b.location(Location(tundra)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(ferret_white.configure(5, 3))
            b.add(polar_bear.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(1, 90):
            b.add(frostmaw.configure(1, 1))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 30):
            b.add(doe_new_zealand.configure(25, 4))


with b.location(Location(earth)):
    with b.active_periods([Range(17000, 19000)]):
        with b.spawn(3, 60):
            b.add(enderman.configure(10, 3))


with b.location(Location(earth.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.light(upper=0):
                with b.spawn(20, 60):
                    b.add(cave_spider.configure(25, 3))

        with b.altitude(upper=24):
            with b.light(upper=0):
                with b.spawn(20, 60):
                    b.add(zotzpyre.configure(25, 3))


with b.location(Location(BiomeSet.ANY)):
    with b.active_periods(ANY):
        with b.spawn(0, 1):
            b.add(chicken)
            b.add(cow)
            b.add(Creature("minecraft:donkey"))
            b.add(Creature("minecraft:horse"))
            b.add(creeper)
            b.add(enderman)
            b.add(husk)
            b.add(llama)
            b.add(mooshroom)
            b.add(pig)
            b.add(rabbit)
            b.add(sheep)
            b.add(skeleton)
            b.add(spider)
            b.add(squid)
            b.add(stray)
            b.add(witch)
            b.add(wolf)
            b.add(zombie)
            b.add(zombie_villager)

config = ConfigFileSet(*b.spawns)
