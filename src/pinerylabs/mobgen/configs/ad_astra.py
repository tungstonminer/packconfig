"""Define the entity generation settings for Ad Astra."""

from pinerylabs.mobgen import BiomeSet, ConfigFileSet, Creature, Location, Range, SpawnBuilder
from pinerylabs.oregen import Ore, OreList
from pinerylabs.oregen.data import vanilla as mc


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


# Animals ##############################################################################################################

albatross = Creature("zawa:albatross", LONER)
alligator = Creature("zawa:indiangharial", PAIR)
anaconda = Creature("zawa:greenanaconda", LONER)
baby_foliaath = Creature("mowziesmobs:baby_foliaath", CLUSTER)
basalz = Creature("thermalfoundation:basalz", CLUSTER)
bat = Creature("minecraft:bat")
bear_grizzly = Creature("zawa:grizzlybear", PAIR)
bear_polar = Creature("zawa:polarbear", LONER)
beaver = Creature("zawa:beaver", PAIR)
bison = Creature("zawa:americanbison", SWARM)
blaze = Creature("minecraft:blaze", CLUSTER)
blitz = Creature("thermalfoundation:blitz", CLUSTER)
blizz = Creature("thermalfoundation:blizz", CLUSTER)
bluefish = Creature("zawa:bluefish", SWARM)
cassowary = Creature("zawa:cassowary", PAIR)
cave_spider = Creature("minecraft:cave_spider", LONER)
chicken = Creature("minecraft:chicken", TROOP)
chimp = Creature("zawa:commonchimpanzee", TROOP)
cichlid = Creature("zawa:cichlid", HERD)
clownfish = Creature("zawa:clownfish", CLUSTER)
coatimundi = Creature("zawa:coatimundi", TROOP)
cockatoo = Creature("zawa:cockatoo", TROOP)
condor = Creature("zawa:andeancondor", PAIR)
cow = Creature("minecraft:cow", PAIR)
crab = Creature("zawa:coconutcrab", CLUSTER)
creeper = Creature("minecraft:creeper", LONER)
dolphin_ocean = Creature("zawa:bottlenosedolphin", HERD)
dolphin_river = Creature("zawa:amazonriverdolphin", CLUSTER)
donkey = Creature("minecraft:donkey", PAIR)
eagle_bald = Creature("zawa:baldeagle", PAIR)
eagle_harpy = Creature("zawa:harpyeagle", PAIR)
echidna = Creature("zawa:echidna", LONER)
eel = Creature("zawa:morayeel", LONER)
elephant = Creature("zawa:africanelephant", HERD)
elephant_asian = Creature("zawa:asianelephant", CLUSTER)
enderman = Creature("minecraft:enderman", CLUSTER)
foliaath = Creature("mowziesmobs:foliaath", LONER)
frigate = Creature("zawa:frigate", TROOP)
frostmaw = Creature("mowziesmobs:frostmaw", LONER)
gaur = Creature("zawa:gaur", HERD)
ghast = Creature("minecraft:ghast", LONER)
gilamonster = Creature("zawa:gilamonster", LONER)
giraffe = Creature("zawa:reticulatedgiraffe", HERD)
gorilla = Creature("zawa:westernlowlandgorilla", TROOP)
grottol = Creature("mowziesmobs:grottol", CLUSTER)
hippo_nile = Creature("zawa:nilehippopotamus", TROOP)
hippo_pygmy = Creature("zawa:pygmyhippopotamus", PAIR)
horse = Creature("horse_colors:horse_felinoid", HERD)
horse_mc = Creature("minecraft:horse", HERD)
husk = Creature("minecraft:husk", CLUSTER)
iguana_fiji = Creature("zawa:fijibandediguana", PAIR)
iguana_marine = Creature("zawa:marineiguana", PAIR)
iron_golem = Creature("minecraft:villager_golem", LONER)
jaguar = Creature("zawa:jaguar", LONER)
kangaroo = Creature("zawa:redkangaroo", TROOP)
koala = Creature("zawa:koala", CLUSTER)
komododragon = Creature("zawa:komododragon", LONER)
lantern = Creature("mowziesmobs:lantern", CLUSTER)
leopard = Creature("zawa:amurleopard", LONER)
lion = Creature("zawa:africanlion", TROOP)
llama = Creature("minecraft:llama", HERD)
macaw = Creature("zawa:macaw", TROOP)
magma_cube = Creature("minecraft:magma_cube", TROOP)
meerkat = Creature("zawa:meerkat", TROOP)
monkey_spider = Creature("zawa:blackspidermonkey", TROOP)
moose = Creature("zawa:moose", PAIR)
mooshroom = Creature("minecraft:mooshroom", HERD)
mule = Creature("minecraft:mule", HERD, DAY)
naga = Creature("mowziesmobs:naga", PAIR)
ocelot = Creature("minecraft:ocelot", LONER)
octopus = Creature("zawa:octopus", LONER)
okapi = Creature("zawa:okapi", CLUSTER)
orca = Creature("zawa:orca", CLUSTER)
owl = Creature("zawa:greathornedowl", LONER)
panda_red = Creature("zawa:redpanda", PAIR)
pangolin = Creature("zawa:indianpangolin", CLUSTER)
parrot = Creature("minecraft:parrot", TROOP)
pig = Creature("minecraft:pig", PAIR)
platypus = Creature("zawa:platypus", PAIR)
pufferfish = Creature("zawa:pufferfish", CLUSTER)
rabbit = Creature("minecraft:rabbit", CLUSTER)
rat = Creature("zawa:brownrat", TROOP, NIGHT)
rattlesnake = Creature("zawa:rattlesnake", LONER)
rhino_black = Creature("zawa:blackrhinoceros", CLUSTER)
rhino_sumatran = Creature("zawa:sumatranrhinoceros", PAIR)
salamander = Creature("zawa:japanesegiantsalamander", LONER)
salmon = Creature("zawa:sockeyesalmon", SWARM)
sea_turtle = Creature("zawa:hawksbillseaturtle", CLUSTER)
shark_great_white = Creature("zawa:greatwhiteshark", LONER)
shark_tiger = Creature("zawa:tigershark", PAIR)
sheep = Creature("minecraft:sheep", HERD)
skeleton = Creature("minecraft:skeleton", PAIR)
skeleton_horse = Creature("minecraft:skeleton_horse", LONER)
slime = Creature("minecraft:slime", CLUSTER)
sloth = Creature("zawa:threetoedsloth", LONER)
snowman = Creature("minecraft:snowman", LONER)
spider = Creature("minecraft:spider", LONER, NIGHT)
squid = Creature("minecraft:squid", TROOP)
stray = Creature("minecraft:stray", PAIR)
tamarin = Creature("zawa:goldenliontamarin", TROOP)
tang = Creature("zawa:marinetang", HERD)
tapir = Creature("zawa:braziliantapir", PAIR)
tasmanian_devil = Creature("zawa:tasmaniandevil", PAIR)
tiger = Creature("zawa:bengaltiger", LONER)
tortoise = Creature("zawa:galapagostortoise", CLUSTER)
toucan = Creature("zawa:toucan", CLUSTER)
treefrog = Creature("zawa:treefrog", CLUSTER)
walrus = Creature("zawa:pacificwalrus", HERD)
whale_humpback = Creature("zawa:humpbackwhale", CLUSTER)
witch = Creature("minecraft:witch", LONER)
wither_skeleton = Creature("minecraft:wither_skeleton", CLUSTER)
wolf = Creature("minecraft:wolf", TROOP)
zebra = Creature("zawa:grevyszebra", HERD)
zombie = Creature("minecraft:zombie", CLUSTER)
zombie_horse = Creature("minecraft:zombie_horse", LONER)
zombie_pigman = Creature("minecraft:zombie_pigman", SWARM)
zombie_villager = Creature("minecraft:zombie_villager", LONER)

animaltrader = Creature("zawa:animaltrader", LONER)
botanist = Creature("zawa:botanist", LONER)
feedtrader = Creature("zawa:feedtrader", LONER)
poacher = Creature("zawa:poacher", CLUSTER, ANY)
villager = Creature("minecraft:villager", LONER)
zookeeper = Creature("zawa:zookeeper", PAIR)

########################################################################################################################

b = SpawnBuilder()

with b.location(Location(beach_cold)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(walrus.with_rarity(10).with_groups_allowed(5))
            b.add(albatross.with_rarity(2))
            b.add(bear_polar.with_rarity(1))

with b.location(Location(beach_gravel)):
    with b.active_periods(DAY):
        with b.spawn(10, 90):
            b.add(frigate.with_rarity(10).with_groups_allowed(3))
            b.add(albatross.with_rarity(1))

with b.location(Location(beach_sandy)):
    with b.active_periods(DAY):
        with b.spawn(20, 60):
            b.add(frigate.with_rarity(100).with_groups_allowed(5))
            b.add(crab.with_rarity(60).with_groups_allowed(3))
            b.add(iguana_marine.with_rarity(15))
            b.add(tortoise.with_rarity(10))
            b.add(albatross.with_rarity(1))

with b.location(Location(desert)):
    with b.active_periods(DAY):
        with b.spawn(20, 90):
            b.add(pangolin.configure(10, 5))
            b.add(kangaroo.configure(2, 1))
            b.add(rattlesnake.configure(1, 5))

    with b.active_periods(NIGHT):
        with b.spawn(6, 90):
            b.add(rattlesnake.configure(1, 6))

    with b.active_periods(TWILIGHT):
        with b.spawn(3, 90):
            b.add(rabbit.with_rarity(20).with_groups_allowed(2))

with b.location(Location(desert.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.spawn(16, 1):
                b.add(blaze.configure(20, 10))

with b.location(Location(desert, weather="thunder")):
    with b.active_periods(ANY):
        with b.spawn(16, 90):
            b.add(blaze.configure(20, 4))

with b.location(Location(forest_canopy)):
    with b.active_periods(DAY):
        with b.spawn(64, 60):
            b.add(echidna.with_rarity(30).with_groups_allowed(5))
            b.add(mooshroom.with_rarity(20).with_groups_allowed(4))
            b.add(hippo_pygmy.with_rarity(2).with_groups_allowed(2))
            b.add(gorilla.with_rarity(1))

    with b.active_periods(NIGHT):
        with b.spawn(64, 60):
            b.add(treefrog.with_rarity(40).with_groups_allowed(16))
            b.add(echidna.with_rarity(20).with_groups_allowed(4))
            b.add(owl.with_rarity(10).with_groups_allowed(4))
            b.add(lantern.with_rarity(5).with_groups_allowed(8))
            b.add(spider.with_rarity(1))

    with b.active_periods(TWILIGHT):
        with b.spawn(20, 60):
            b.add(rabbit.with_rarity(20).with_groups_allowed(5))

with b.location(Location(forest_ice)):
    with b.active_periods(DAY):
        with b.spawn(20, 30):
            b.add(blizz.configure(20, 10))

    with b.active_periods(NIGHT):
        with b.spawn(20, 30):
            b.add(blizz.configure(20, 10))
            b.add(frostmaw.configure(5, 4))

with b.location(Location(forest_jungle)):
    with b.active_periods(DAY):
        with b.spawn(64, 15):
            b.add(parrot.configure(75, 10))
            b.add(monkey_spider.configure(50, 8))
            b.add(cockatoo.configure(40, 5))
            b.add(macaw.configure(40, 5))
            b.add(toucan.configure(40, 5))
            b.add(sloth.configure(30, 4))
            b.add(tamarin.configure(30, 4))
            b.add(iguana_fiji.configure(25, 3))
            b.add(coatimundi.configure(20, 4))
            b.add(eagle_harpy.configure(10, 4))
            b.add(rhino_sumatran.configure(10, 2))
            b.add(okapi.configure(10, 2))
            b.add(chimp.configure(6, 3))
            b.add(gorilla.configure(3, 2))
            b.add(elephant_asian.configure(2, 2))
            b.add(foliaath.configure(1, 3))
            b.add(baby_foliaath.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(64, 15):
            b.add(treefrog.configure(75, 10))
            b.add(sloth.configure(30, 4))
            b.add(coatimundi.configure(20, 4))
            b.add(tapir.configure(15, 3))
            b.add(rhino_sumatran.configure(10, 2))
            b.add(ocelot.configure(2, 1))
            b.add(jaguar.configure(2, 1))
            b.add(tiger.configure(2, 1))
            b.add(foliaath.configure(1, 3))
            b.add(baby_foliaath.configure(1, 2))

with b.location(Location(forest_temperate)):
    with b.active_periods(DAY):
        with b.spawn(48, 60):
            b.add(echidna.configure(30, 10))
            b.add(koala.configure(10, 5))
            b.add(beaver.configure(5, 3))
            b.add(cassowary.configure(2, 5))
            b.add(eagle_bald.configure(1, 4))

    with b.active_periods(NIGHT):
        with b.spawn(48, 60):
            b.add(echidna.configure(30, 10))
            b.add(owl.configure(20, 8))
            b.add(tasmanian_devil.configure(1, 2))

    with b.active_periods(TWILIGHT):
        with b.spawn(20, 15):
            b.add(rabbit.configure(10, 5))
            b.add(leopard.configure(1, 1))

with b.location(Location(mars.in_cave())):
    with b.active_periods(ANY):
        with b.spawn(16, 1):
            b.add(grottol.configure(20, 10))

with b.location(Location(mesa)):
    with b.active_periods(DAY):
        with b.spawn(20, 90):
            b.add(mule.configure(6, 4))
            b.add(rattlesnake.configure(3, 10))
            b.add(komododragon.configure(1, 5))

    with b.active_periods(NIGHT):
        with b.spawn(20, 90):
            b.add(kangaroo.configure(6, 4))
            b.add(rattlesnake.configure(3, 10))

    with b.active_periods(TWILIGHT):
        with b.spawn(3, 90):
            b.add(rabbit.configure(60, 10))
            b.add(gilamonster.configure(20, 5))

with b.location(Location(mesa.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.spawn(32, 1):
                b.add(blaze.configure(20, 20))

with b.location(Location(mesa, weather="thunder")):
    with b.active_periods(ANY):
        with b.spawn(16, 90):
            b.add(blaze.configure(20, 4))

with b.location(Location(mountain)):
    with b.active_periods(DAY):
        with b.altitude(lower=110):
            with b.spawn(4, 90):
                b.add(naga.configure(1, 2))

        with b.altitude(upper=110):
            with b.spawn(48, 90):
                b.add(llama.configure(20, 10))
                b.add(condor.configure(5, 5))

    with b.active_periods(NIGHT):
        with b.altitude(upper=110):
            with b.spawn(8, 90):
                b.add(wolf.configure(1, 4))

with b.location(Location(mountain.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.spawn(48, 1):
                b.add(basalz.configure(20, 16))

        with b.spawn(16, 1):
            b.add(iron_golem.configure(10, 8))

with b.location(Location(mountain, weather="thunder")):
    with b.active_periods(ANY):
        with b.spawn(16, 90):
            b.add(basalz.configure(20, 4))

with b.location(Location(mountain_forest)):
    with b.active_periods(DAY):
        with b.spawn(32, 90):
            b.add(sheep.configure(10, 4))
            b.add(mule.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(32, 90):
            b.add(owl.configure(20, 4))
            b.add(panda_red.configure(10, 4))
            b.add(wolf.configure(1, 2))

    with b.active_periods(TWILIGHT):
        with b.spawn(32, 90):
            b.add(rabbit.configure(20, 4))

with b.location(Location(mushroom)):
    with b.active_periods(DAY):
        with b.spawn(32, 30):
            b.add(mooshroom.configure(20, 10))

with b.location(Location(ocean)):
    with b.active_periods(ANY):
        with b.spawn(128, 30):
            b.add(bluefish.configure(100, 20))
            b.add(clownfish.configure(40, 10))
            b.add(tang.configure(40, 10))
            b.add(pufferfish.configure(40, 5))
            b.add(tortoise.configure(25, 10))
            b.add(sea_turtle.configure(25, 10))
            b.add(octopus.configure(20, 10))
            b.add(eel.configure(20, 4))
            b.add(dolphin_ocean.configure(2, 1))
            b.add(shark_tiger.configure(1, 2))
            b.add(orca.configure(1, 1))

with b.location(Location(ocean_deep)):
    with b.active_periods(ANY):
        with b.spawn(64, 90):
            b.add(bluefish.configure(100, 30))
            b.add(squid.configure(50, 20))
            b.add(octopus.configure(20, 10))
            b.add(dolphin_ocean.configure(10, 1))
            b.add(orca.configure(4, 1))
            b.add(whale_humpback.configure(2, 1))
            b.add(shark_great_white.configure(1, 1))

with b.location(Location(ocean_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(128, 120):
            b.add(bluefish.configure(50, 40))
            b.add(octopus.configure(5, 20))
            b.add(orca.configure(1, 1))

with b.location(Location(nether)):
    with b.active_periods(ANY):
        with b.spawn(32, 90):
            b.add(skeleton.configure(8, 8))
            b.add(zombie.configure(4, 2))
            b.add(zombie_villager.configure(1, 2))

with b.location(Location(plains)):
    with b.active_periods(DAY):
        with b.spawn(40, 60):
            b.add(bison.with_rarity(5).with_groups_allowed(5))
            b.add(horse.with_rarity(1).with_groups_allowed(3))

    with b.active_periods(TWILIGHT):
        with b.spawn(40, 60):
            b.add(rabbit.with_groups_allowed(20)),

with b.location(Location(BiomeSet.merge(plains, savanna).in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.spawn(16, 1):
                b.add(blitz.configure(20, 10))

with b.location(Location(BiomeSet.merge(plains, savanna), weather="thunder")):
    with b.active_periods(ANY):
        with b.spawn(16, 90):
            b.add(blitz.configure(20, 4))

with b.location(Location(river.in_water())):
    with b.active_periods(ANY):
        with b.spawn(64, 60):
            b.add(bluefish.configure(16, 20))
            b.add(salmon.configure(8, 10))
            b.add(cichlid.configure(4, 5))
            b.add(pufferfish.configure(2, 5))
            b.add(salamander.configure(1, 1))

with b.location(Location(river_frozen.in_water())):
    with b.active_periods(ANY):
        with b.spawn(32, 120):
            b.add(salmon.configure(3, 16))
            b.add(bluefish.configure(1, 16))

with b.location(Location(savanna)):
    with b.active_periods(DAY):
        with b.spawn(32, 90):
            b.add(meerkat.configure(8, 16))
            b.add(zebra.configure(6, 4))
            b.add(elephant.configure(4, 4))
            b.add(gaur.configure(3, 2))
            b.add(giraffe.configure(2, 2))
            b.add(chimp.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(32, 90):
            b.add(meerkat.configure(8, 16))
            b.add(elephant.configure(4, 4))
            b.add(giraffe.configure(2, 2))
            b.add(rhino_black.configure(1, 2))

    with b.active_periods(TWILIGHT):
        with b.spawn(8, 45):
            b.add(lion.configure(1, 2))

village_blocks = [Ore("minecraft:grass_path"), mc.dirt, mc.grass, mc.gravel, Ore("minecraft:log")]
with b.location(Location(settled.with_blocks(village_blocks), structure="Village")):
    with b.active_periods(DAY):
        with b.spawn(20, 1):
            b.add(chicken.configure(40, 1))
            b.add(pig.configure(30, 1))
            b.add(cow.configure(15, 1))
            b.add(donkey.configure(10, 1))
            b.add(iron_golem.configure(1, 1))

    with b.active_periods(NIGHT):
        with b.spawn(10, 1):
            b.add(rat.configure(20, 4))

with b.location(Location(settled.in_cave().with_blocks(mc.cobblestone, mc.dirt, mc.planks), structure="Village")):
    with b.active_periods(NIGHT):
        with b.spawn(4, 60):
            b.add(villager.with_rarity(1).with_groups_allowed(4))

with b.location(Location(swamp)):
    with b.active_periods(DAY):
        with b.spawn(64, 15):
            b.add(alligator.configure(10, 4))
            b.add(platypus.configure(10, 5))
            b.add(slime.configure(1, 3))

    with b.active_periods(NIGHT):
        with b.spawn(96, 15):
            b.add(alligator.configure(25, 4))
            b.add(slime.configure(20, 3))
            b.add(hippo_nile.configure(20, 1))
            b.add(anaconda.configure(2, 2))
            b.add(jaguar.configure(1, 1))

    with b.active_periods(TWILIGHT):
        with b.spawn(10, 7):
            b.add(rhino_sumatran.configure(1, 1))

with b.location(Location(swamp.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=24):
            with b.spawn(16, 1):
                b.add(grottol.configure(20, 3))

with b.location(Location(swamp.in_water())):
    with b.active_periods(ANY):
        with b.spawn(128, 30):
            b.add(bluefish.configure(8, 20))
            b.add(cichlid.configure(4, 15))
            b.add(salamander.configure(1, 10))

with b.location(Location(swamp, weather="rain")):
    with b.active_periods(ANY):
        with b.spawn(64, 15):
            b.add(slime.configure(20, 10))

# TODO: check this
with b.location(Location(swamp, structure="Temple")):
    with b.active_periods(ANY):
        with b.spawn(1, 1):
            b.add(witch.configure(20, 1))

with b.location(Location(BiomeSet.merge(taiga, taiga_snowy))):
    with b.active_periods(DAY):
        with b.spawn(48, 60):
            b.add(sheep.configure(30, 8))
            b.add(eagle_bald.configure(6, 8))
            b.add(moose.configure(3, 4))
            b.add(bear_grizzly.configure(1, 2))

    with b.active_periods(NIGHT):
        with b.spawn(64, 60):
            b.add(rat.configure(5, 45))
            b.add(owl.configure(1, 15))
            b.add(wolf.configure(1, 10))

    with b.active_periods(TWILIGHT):
        with b.spawn(20, 45):
            b.add(rabbit.configure(1, 5))

with b.location(Location(the_end)):
    with b.active_periods(ANY):
        with b.spawn(64, 30):
            b.add(enderman.configure(20, 10))

with b.location(Location(tundra)):
    with b.active_periods(DAY):
        with b.spawn(4, 120):
            b.add(bear_polar.configure(10, 2))

    with b.active_periods(NIGHT):
        with b.spawn(2, 120):
            b.add(frostmaw.configure(1, 2))

with b.location(Location(tundra.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(upper=48):
            with b.spawn(16, 1):
                b.add(blizz.configure(20, 10))

with b.location(Location(tundra, weather="thunder")):
    with b.active_periods(ANY):
        with b.spawn(16, 45):
            b.add(blizz.configure(20, 4))

with b.location(Location(BiomeSet.ANY)):
    with b.active_periods([Range(17000, 19000)]):
        with b.spawn(2, 300):
            b.add(enderman.configure(1, 1))

with b.location(Location(earth)):
    with b.active_periods(NIGHT):
        with b.spawn(16, 60):
            b.add(bat.configure(1, 4))

with b.location(Location(earth.in_cave())):
    with b.active_periods(ANY):
        with b.altitude(lower=48):
            with b.spawn(32, 1):
                b.add(rat.configure(10, 16))
                b.add(bat.configure(10, 16))
                b.add(cave_spider.configure(1, 8))

with b.location(Location(BiomeSet.ANY)):
    with b.active_periods(ANY):
        with b.spawn(0, 1):
            b.add(squid)

            b.add(chicken)
            b.add(cow)
            b.add(donkey)
            b.add(Creature("minecraft:horse"))
            b.add(horse)
            b.add(llama)
            b.add(pig)
            b.add(rabbit)
            b.add(sheep)
            b.add(wolf)

            b.add(creeper)
            b.add(enderman)
            b.add(skeleton)
            b.add(spider)
            b.add(stray)
            b.add(witch)
            b.add(zombie)
            b.add(zombie_villager)

config = ConfigFileSet(*b.spawns)
