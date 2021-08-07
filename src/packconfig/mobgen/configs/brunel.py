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
HELLISH = OreList(mc.netherrack, mc.soul_sand, mc.nether_brick, mc.bedrock, mc.stone)
MOLTEN = OreList(mc.lava)
SANDY = OreList(mc.dirt, mc.sand, mc.sandstone)
SNOWY = OreList(mc.dirt, mc.gravel, mc.ice, mc.sand, mc.snow)
STONY = OreList(mc.cobblestone, mc.stone)
SWAMPY = OreList(mc.dirt, mc.grass, mc.sand, mc.water)

MOUNTAINOUS = OreList(
    mc.cobblestone, mc.stone, mc.grass, mc.gravel, Ore("chisel:marble2"), Ore("minecraft:stained_hardened_clay"),
    Ore("minecraft:snow_layer"),
)


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
mountain = BiomeSet("Extreme Hills", "Extreme Hills M", "Extreme Hills Edge", blocks=MOUNTAINOUS)
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
arrow = "minecraft:arrow"
bearhead_brown = "betteranimalsplus:bearhead_1"
bearhead_black = "betteranimalsplus:bearhead_2"
bearhead_polar = "betteranimalsplus:bearhead_3"
blaze_powder = "minecraft:blaze_powder"
blaze_rod = "minecraft:blaze_rod"
blubber = "betteranimalsplus:blubber"
bone = "minecraft:bone"
bone_meal = "minecraft:dye:15"
bottle_o_enchanting = "minecraft:experience_bottle"
carcass_chicken = "minecraft:chicken"
carcass_clownfish = "minecraft:fish:2"
carcass_crab = "harvestcraft:crabrawitem"
carcass_eel1 = "betteranimalsplus:eel_meat_raw"
carcass_eel2 = "harvestcraft:eelrawitem"
carcass_fish = "minecraft:fish"
carcass_frog = "harvestcraft:frograwitem"
carcass_octopus = "harvestcraft:octopusrawitem"
carcass_pheasant = "betteranimalsplus:pheasantraw"
carcass_pufferfish = "minecraft:fish:3"
carcass_rabbit = "minecraft:rabbit"
carcass_salmon = "minecraft:fish:1"
carcass_squid = "harvestcraft:calamarirawitem"
carcass_turkey = "betteranimalsplus:turkey_raw"
egg_chicken_white = "minecraft:egg"
egg_goose = "betteranimalsplus:goose_egg"
egg_goose_golden = "betteranimalsplus:golden_goose_egg"
egg_pheasant = "betteranimalsplus:pheasant_egg"
egg_turkey = "betteranimalsplus:turkey_egg"
emerald = "minecraft:emerald"
ender_pearl = "minecraft:ender_pearl"
feather = "minecraft:feather"
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
meat_beef = "minecraft:beef"
meat_bird = "harvestcraft:groundchickenitem"
meat_crab = "betteranimalsplus:crab_meat_raw"
meat_duck = "harvestcraft:duckrawitem"
meat_eel = "betteranimalsplus:eel_meat_raw"
meat_fish = "harvestcraft:groundfishitem"
meat_mutton = "minecraft:mutton"
meat_pork = "minecraft:porkchop"
meat_turkey_leg = "betteranimalsplus:turkey_leg_raw"
meat_venison = "harvestcraft:venisonrawitem"
mushroom_item = "minecraft:red_mushroom"
naga_fang = "mowziesmobs:naga_fang"
prismarine_shard = "minecraft:prismarine_shard"
rabbit_foot = "minecraft:rabbit_foot"
silver_nugget = "agricraft:agri_nugget:7"
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
bird_tiny_loot = [Loot("1-2", feather)]
blaze_loot = [Loot("1-3", blaze_rod), Loot("1-3", blaze_powder)]
boar_loot = [Loot("2-4", meat_pork), Loot("1-2", hide_large)]
chicken_loot = [Loot("1", carcass_chicken), Loot("0-1", feather), Loot("0-1", bone)]
cow_loot = [Loot("3-4", meat_beef), Loot("1-2", hide_large), Loot("2-3", bone)]
coyote_loot = default_loot
crab_loot = [Loot("1", carcass_crab), Loot("0-1", meat_crab)]
creeper_loot = [Loot("2-4", gunpowder)]
deer_loot = default_loot
donkey_loot = [Loot("1", hide_large), Loot("1", bone)]
eel_freshwater_loot = [Loot("1-2", carcass_eel1)]
eel_saltwater_loot = [Loot("1-2", carcass_eel2)]
enderman_loot = [Loot("1-2", ender_pearl)]
evocation_illager_loot = default_loot
feralwolf_loot = default_loot
foliaath_baby_loot = default_loot
foliaath_loot = default_loot
fox_loot = [Loot("1", hide_small)]
frostmaw_loot = default_loot
ghast_loot = default_loot
goose_loot = chicken_loot
grottol_loot = default_loot
hirschgeist_loot = [Loot("1", hirschgeist_skull), Loot("2-3", bone)]
horse_loot = [Loot("1", hide_large), Loot("1-2", meat_venison), Loot("0-1", bone)]
horseshoecrab_loot = [Loot("1-2", meat_crab)]
husk_loot = default_loot
illusion_illager_loot = default_loot
jellyfish_loot = default_loot
lammergeier_loot = default_loot
lamprey_loot = default_loot
lantern_loot = default_loot
llama_loot = [Loot("1-2", wool), Loot("1", meat_venison), Loot("1-2", bone)]
magma_cube_loot = [Loot("1-2", magma_cream)]
mammal_small_loot = [Loot("1", hide_small)]
moose_loot = default_loot
mooshroom_loot = [Loot("1-2", meat_beef), Loot("0-1", hide_large), Loot("1-2", mushroom_item)]
mule_loot = [Loot("1", hide_large), Loot("1-2", meat_venison), Loot("1-2", bone)]
naga_loot = default_loot
nautilus_loot = default_loot
ocelot_loot = default_loot
octopus_loot = [Loot("1-2", carcass_octopus), Loot("0-2", ink_sac)]
parrot_loot = bird_tiny_loot
pheasant_loot = [Loot("1-2", carcass_pheasant), Loot("0-1", feather)]
rabbit_loot = [Loot("1", carcass_rabbit), Loot("0-1", hide_small), Loot("0-2",  rabbit_foot)]
reindeer_loot = [Loot("1-2", meat_venison), Loot("0-2", antler)]
shark_loot = default_loot
shulker_loot = default_loot
silverfish_loot = [Loot("0-1", meat_crab), Loot("0-1", silver_nugget)]
skeleton_horse_loot = [Loot("2-3", bone)]
skeleton_loot = [Loot("1-2", bone), Loot("0-4", arrow)]
slime_loot = [Loot("1-2", slime_ball)]
snowman_loot = [Loot("8-12", snowball)]
spider_loot = [Loot("1-4", spider_eye), Loot("0-1", meat_crab)]
squid_loot = [Loot("1", carcass_squid), Loot("1-2", ink_sac)]
stray_loot = default_loot
turkey_loot = [Loot("1", carcass_turkey), Loot("0-2", meat_turkey_leg), Loot("1-2", feather)]
vex_loot = default_loot
villager_golem_loot = default_loot
villager_loot = default_loot
vindication_illager_loot = default_loot
walrus_loot = [Loot("3-4", blubber), Loot("2-3", meat_beef), Loot("1-2", bone), Loot("1", hide_large)]
whale_loot = [Loot("5-7", blubber), Loot("4-6", meat_beef), Loot("3-5", bone), Loot("2-3", hide_large)]
witch_loot = default_loot
wither_loot = default_loot
wither_skeleton_loot = default_loot
wolf_loot = default_loot
zombie_horse_loot = default_loot
zombie_loot = default_loot
zombie_pigman_loot = default_loot
zombie_villager_loot = default_loot
zotzpyre_loot = [Loot("2-3", hide_small)]

# Entities #############################################################################################################

badger = Creature("betteranimalsplus:badger", LONER, loot_list=mammal_small_loot)
bat = Creature("minecraft:bat", HERD, loot_list=no_loot)
blackbear = Creature("betteranimalsplus:blackbear", PAIR, loot_list=bear_black_loot)
blaze = Creature("minecraft:blaze", CLUSTER, loot_list=blaze_loot)
boar = Creature("betteranimalsplus:boar", TROOP, loot_list=boar_loot)
bobbit_worm = Creature("betteranimalsplus:bobbit_worm", LONER, loot_list=no_loot)
brownbear = Creature("betteranimalsplus:brownbear", PAIR, loot_list=bear_brown_loot)
cave_spider = Creature("minecraft:cave_spider", LONER, loot_list=spider_loot)
chicken = Creature("minecraft:chicken", LONER, loot_list=chicken_loot)
cow = Creature("minecraft:cow", HERD, loot_list=cow_loot)
coyote = Creature("betteranimalsplus:coyote", CLUSTER, loot_list=coyote_loot)
crab = Creature("betteranimalsplus:crab", LONER, loot_list=crab_loot)
creeper = Creature("minecraft:creeper", LONER, loot_list=creeper_loot)
deer = Creature("betteranimalsplus:deer", PAIR, loot_list=deer_loot)
donkey = Creature("horse_colors:donkey", TROOP, loot_list=donkey_loot)
eel_freshwater = Creature("betteranimalsplus:eel_freshwater", CLUSTER, loot_list=eel_freshwater_loot)
eel_saltwater = Creature("betteranimalsplus:eel_saltwater", CLUSTER, loot_list=eel_saltwater_loot)
enderman = Creature("minecraft:enderman", LONER, loot_list=enderman_loot)
evocation_illager = Creature("minecraft:evocation_illager", CLUSTER, loot_list=evocation_illager_loot)
feralwolf = Creature("betteranimalsplus:feralwolf", CLUSTER, loot_list=feralwolf_loot)
foliaath = Creature("mowziesmobs:foliaath", LONER, loot_list=foliaath_loot)
foliaath_baby = Creature("mowziesmobs:baby_foliaath", LONER, loot_list=foliaath_baby_loot)
fox = Creature("betteranimalsplus:fox", PAIR, loot_list=fox_loot)
frostmaw = Creature("mowziesmobs:frostmaw", LONER, loot_list=frostmaw_loot)
ghast = Creature("minecraft:ghast", LONER, loot_list=ghast_loot)
goose = Creature("betteranimalsplus:goose", TROOP, loot_list=goose_loot)
grottol = Creature("mowziesmobs:grottol", LONER, loot_list=grottol_loot)
hirschgeist = Creature("betteranimalsplus:hirschgeist", LONER, loot_list=hirschgeist_loot)
horse = Creature("horse_colors:horse_felinoid", HERD, loot_list=horse_loot)
horseshoecrab = Creature("betteranimalsplus:horseshoecrab", LONER, loot_list=horseshoecrab_loot)
husk = Creature("minecraft:husk", LONER, loot_list=husk_loot)
illusion_illager = Creature("minecraft:illusion_illager", LONER, loot_list=illusion_illager_loot)
jellyfish = Creature("betteranimalsplus:jellyfish", SWARM, loot_list=jellyfish_loot)
lammergeier = Creature("betteranimalsplus:lammergeier", LONER, loot_list=lammergeier_loot)
lamprey = Creature("betteranimalsplus:lamprey", CLUSTER, loot_list=lamprey_loot)
lantern = Creature("mowziesmobs:lantern", LONER, loot_list=lantern_loot)
llama = Creature("minecraft:llama", HERD, loot_list=llama_loot)
magma_cube = Creature("minecraft:magma_cube", LONER, loot_list=magma_cube_loot)
moose = Creature("betteranimalsplus:moose", PAIR, loot_list=moose_loot)
mooshroom = Creature("minecraft:mooshroom", HERD, loot_list=default_loot)
mule = Creature("horse_colors:mule", CLUSTER, loot_list=mule_loot)
naga = Creature("mowziesmobs:naga", LONER, loot_list=naga_loot)
nautilus = Creature("betteranimalsplus:nautilus", SWARM, loot_list=nautilus_loot)
ocelot = Creature("minecraft:ocelot", LONER, loot_list=ocelot_loot)
parrot = Creature("minecraft:parrot", CLUSTER, loot_list=default_loot)
pheasant = Creature("betteranimalsplus:pheasant", TROOP, loot_list=pheasant_loot)
pig = Creature("minecraft:pig", TROOP, loot_list=default_loot)
polar_bear = Creature("minecraft:polar_bear", LONER, loot_list=bear_polar_loot)
rabbit = Creature("minecraft:rabbit", CLUSTER, loot_list=rabbit_loot)
reindeer = Creature("betteranimalsplus:reindeer", HERD, loot_list=reindeer_loot)
shark = Creature("betteranimalsplus:shark", CLUSTER, loot_list=shark_loot)
sheep = Creature("minecraft:sheep", LONER, loot_list=default_loot)
shulker = Creature("minecraft:shulker", CLUSTER, loot_list=shulker_loot)
silverfish = Creature("minecraft:silverfish", CLUSTER, loot_list=silverfish_loot)
skeleton = Creature("minecraft:skeleton", CLUSTER, loot_list=skeleton_loot)
skeleton_horse = Creature("minecraft:skeleton_horse", CLUSTER, loot_list=skeleton_horse_loot)
slime = Creature("minecraft:slime", LONER, loot_list=slime_loot)
snowman = Creature("minecraft:snowman", LONER, loot_list=snowman_loot)
songbird = Creature("betteranimalsplus:songbird", CLUSTER, loot_list=bird_tiny_loot)
spider = Creature("minecraft:spider", LONER, loot_list=spider_loot)
squid = Creature("minecraft:squid", CLUSTER, loot_list=squid_loot)
squirrel = Creature("betteranimalsplus:squirrel", PAIR, loot_list=mammal_small_loot)
stray = Creature("minecraft:stray", CLUSTER, loot_list=stray_loot)
tarantula = Creature("betteranimalsplus:tarantula", LONER, loot_list=spider_loot)
turkey = Creature("betteranimalsplus:turkey", TROOP, loot_list=turkey_loot)
vex = Creature("minecraft:vex", LONER, loot_list=vex_loot)
villager = Creature("minecraft:villager", TROOP, loot_list=villager_loot)
villager_golem = Creature("minecraft:villager_golem", LONER, loot_list=villager_golem_loot)
vindication_illager = Creature("minecraft:vindication_illager", LONER, loot_list=vindication_illager_loot)
walrus = Creature("betteranimalsplus:walrus", HERD, loot_list=walrus_loot)
whale = Creature("betteranimalsplus:whale", HERD, loot_list=whale_loot)
witch = Creature("minecraft:witch", LONER, loot_list=witch_loot)
wither = Creature("minecraft:wither", LONER, loot_list=wither_loot)
wither_skeleton = Creature("minecraft:wither_skeleton", LONER, loot_list=wither_skeleton_loot)
wolf = Creature("minecraft:wolf", CLUSTER, loot_list=wolf_loot)
zombie = Creature("minecraft:zombie", LONER, loot_list=zombie_loot)
zombie_horse = Creature("minecraft:zombie_horse", LONER, loot_list=zombie_horse_loot)
zombie_pigman = Creature("minecraft:zombie_pigman", LONER, loot_list=zombie_pigman_loot)
zombie_villager = Creature("minecraft:zombie_villager", LONER, loot_list=zombie_villager_loot)
zotzpyre = Creature("betteranimalsplus:zotzpyre", LONER, loot_list=zotzpyre_loot)

# Entity Spawn ####################################################################################################

b = SpawnBuilder()

with b.location(Location(beach_cold)):
    with b.active_periods(DAY):
        with b.spawn(5, 15):
            b.add(horseshoecrab.configure(10, 3))


with b.location(Location(beach_gravel)):
    with b.active_periods(DAY):
        with b.spawn(4, 90):
            b.add(walrus.configure(25, 3))


with b.location(Location(beach_sandy)):
    with b.active_periods(DAY):
        with b.spawn(5, 15):
            b.add(crab.configure(25, 3))


with b.location(Location(desert)):
    with b.active_periods(DAY):
        with b.spawn(5, 90):
            pass

    with b.active_periods(NIGHT):
        with b.spawn(2, 90):
            b.add(tarantula.configure(1, 3))

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 15):
            b.add(rabbit.configure(15, 3))


with b.location(Location(desert.in_cave().with_blocks(HELLISH))):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.light(upper=0):
                with b.spawn(32, 15):
                    b.add(blaze.configure(5, 10))


with b.location(Location(forest_canopy)):
    with b.active_periods(DAY):
        with b.spawn(20, 30):
            pass

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 15):
            pass

    with b.active_periods(NIGHT):
        with b.spawn(6, 90):
            b.add(spider.configure(10, 2))


with b.location(Location(forest_hills)):
    with b.active_periods(DAY):
        with b.spawn(15, 90):
            b.add(pheasant.configure(40, 5))
            b.add(badger.configure(10, 2))
            b.add(blackbear.configure(1, 1))

    with b.active_periods(NIGHT):
        with b.spawn(2, 90):
            b.add(fox.configure(10, 5))


with b.location(Location(forest_ice)):
    with b.active_periods(ANY):
        with b.spawn(1, 120):
            b.add(frostmaw.configure(1, 1))


with b.location(Location(forest_jungle)):
    with b.active_periods(DAY):
        with b.spawn(20, 30):
            b.add(parrot.configure(60, 5))
            b.add(chicken.configure(30, 4))

    with b.active_periods(NIGHT):
        with b.spawn(5, 30):
            b.add(ocelot.configure(5, 2))

    with b.active_periods(ANY):
        with b.spawn(1, 150):
            b.add(foliaath.configure(2, 1))


with b.location(Location(forest_temperate)):
    with b.active_periods(DAY):
        with b.spawn(20, 30):
            b.add(squirrel.configure(50, 4))
            b.add(songbird.configure(50, 4))
            b.add(deer.configure(25, 2))

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 15):
            b.add(rabbit.configure(25, 3))

    with b.active_periods(NIGHT):
        with b.spawn(2, 30):
            b.add(fox.configure(25, 3))


with b.location(Location(mesa)):
    with b.active_periods(DAY):
        with b.spawn(5, 90):
            b.add(donkey.configure(10, 2))

    with b.active_periods(NIGHT):
        with b.spawn(5, 60):
            b.add(coyote.configure(25, 3))


with b.location(Location(mesa.in_cave())):
    with b.active_periods(ANY):
        with b.light(upper=0):
            with b.spawn(32, 90):
                b.add(blaze.configure(5, 10))


with b.location(Location(mountain)):
    with b.active_periods(DAY):
        with b.altitude(lower=110):
            with b.spawn(10, 90):
                b.add(lammergeier.configure(25, 5))
                b.add(naga.configure(5, 3))

        with b.altitude(upper=110):
            with b.spawn(15, 90):
                b.add(llama.configure(5, 3))

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 15):
            pass

    with b.active_periods(NIGHT):
        with b.altitude(upper=110):
            with b.spawn(5, 60):
                b.add(wolf.configure(25, 3))

with b.location(Location(mountain.in_cave())):
    with b.active_periods(ANY):
        with b.spawn(4, 90):
            b.add(villager_golem.configure(1, 1))


with b.location(Location(mountain_forest)):
    with b.active_periods(DAY):
        with b.spawn(10, 60):
            b.add(sheep.configure(15, 2))

    with b.active_periods(NIGHT):
        with b.spawn(3, 60):
            pass


with b.location(Location(mushroom)):
    with b.active_periods(ANY):
        with b.spawn(30, 30):
            b.add(mooshroom.configure(100, 6))


with b.location(Location(ocean)):
    with b.active_periods(ANY):
        with b.spawn(30, 30):
            b.add(squid.configure(50, 5))
            b.add(eel_saltwater.configure(40, 4))
            b.add(jellyfish.configure(30, 3))
            b.add(bobbit_worm.configure(5, 2))


with b.location(Location(ocean_deep)):
    with b.active_periods(ANY):
        with b.spawn(45, 60):
            b.add(nautilus.configure(20, 4))
            b.add(jellyfish.configure(15, 2))
            b.add(shark.configure(10, 1))
            b.add(whale.configure(5, 1))


with b.location(Location(ocean_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(10, 90):
            b.add(whale.configure(5, 1))


with b.location(Location(nether)):
    with b.active_periods(ANY):
        with b.spawn(20, 15):
            b.add(skeleton.configure(20, 5))
            b.add(zombie.configure(10, 4))
            b.add(zombie_villager.configure(5, 3))


with b.location(Location(plains)):
    with b.active_periods(DAY):
        with b.spawn(15, 60):
            b.add(cow.configure(20, 1))

    with b.active_periods(NIGHT):
        with b.spawn(5, 60):
            pass

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 15):
            b.add(rabbit.configure(25, 2))


with b.location(Location(river.in_water())):
    with b.active_periods(ANY):
        with b.spawn(10, 60):
            b.add(eel_freshwater.configure(25, 3))


with b.location(Location(river_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(20, 60):
            pass


with b.location(Location(savanna)):
    with b.active_periods(DAY):
        with b.spawn(10, 60):
            b.add(cow.configure(20, 1))
            b.add(horse.configure(10, 1))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 15):
            b.add(rabbit.configure(25, 2))


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
        with b.spawn(20, 30):
            b.add(pig.configure(30, 5))
            b.add(goose.configure(20, 3))

    with b.active_periods(NIGHT):
        with b.spawn(5, 60):
            b.add(slime.configure(25, 2))


with b.location(Location(swamp.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=24):
            with b.spawn(3, 90):
                b.add(grottol.configure(5, 3))


with b.location(Location(swamp.in_water())):
    with b.active_periods(ANY):
        with b.spawn(15, 15):
            b.add(eel_freshwater.configure(20, 3))
            b.add(lamprey.configure(10, 3))


with b.location(Location(swamp, weather="rain")):
    with b.active_periods(ANY):
        with b.spawn(10, 15):
            b.add(slime.configure(50, 3))


with b.location(Location(swamp, structure="Temple")):
    with b.active_periods(ANY):
        with b.spawn(1, 1):
            b.add(witch.configure(100, 1))


with b.location(Location(taiga)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(turkey.configure(20, 3))
            b.add(sheep.configure(15, 3))
            b.add(brownbear.configure(5, 1))

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 30):
            b.add(rabbit.configure(40, 3))


with b.location(Location(taiga_hills)):
    with b.active_periods(DAY):
        with b.spawn(10, 60):
            b.add(sheep.configure(30, 4))
            b.add(moose.configure(10, 1))

    with b.active_periods(NIGHT):
        with b.spawn(5, 60):
            b.add(wolf.configure(25, 1))


with b.location(Location(taiga_snowy)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(reindeer.configure(20, 2))

    with b.active_periods(NIGHT):
        with b.spawn(1, 90):
            b.add(hirschgeist.configure(1, 3))

    with b.active_periods(NIGHT):
        with b.spawn(5, 90):
            b.add(feralwolf.configure(5, 1))


with b.location(Location(the_end)):
    with b.active_periods(ANY):
        with b.spawn(80, 15):
            b.add(enderman.configure(100, 20, Range(1, 4)))


with b.location(Location(tundra)):
    with b.active_periods(DAY):
        with b.spawn(5, 90):
            b.add(polar_bear.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(1, 90):
            b.add(frostmaw.configure(1, 1))

    with b.active_periods(TWILIGHT):
        with b.spawn(5, 30):
            pass


with b.location(Location(earth)):
    with b.active_periods([Range(17000, 19000)]):
        with b.spawn(3, 60):
            b.add(enderman.configure(10, 3))


with b.location(Location(earth.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.light(upper=0):
                with b.spawn(15, 60):
                    b.add(cave_spider.configure(25, 3))

        with b.altitude(upper=24):
            with b.light(upper=0):
                with b.spawn(10, 60):
                    b.add(zotzpyre.configure(25, 3))


with b.location(Location(BiomeSet.ANY)):
    with b.active_periods(ANY):
        with b.spawn(0, 1):
            b.add(Creature("minecraft:donkey"))
            b.add(Creature("minecraft:horse"))
            b.add(creeper)
            b.add(enderman)
            b.add(husk)
            b.add(skeleton)
            b.add(squid)
            b.add(stray)
            b.add(witch)
            b.add(zombie)
            b.add(zombie_villager)

config = ConfigFileSet(*b.spawns)
