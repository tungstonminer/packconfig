"""Define the entity generation settings for Ad Astra."""

from pinerylabs.mobgen import BiomeSet, ConfigFileSet, Creature, Location, Loot, Range, SpawnBuilder
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


# Loot Items  ##########################################################################################################

basalz_powder = "thermalfoundation:material:2053"
basalz_rod = "thermalfoundation:material:2052"
bird_carcass = "minecraft:chicken"
bird_meat = "zawa:bird_meat"
blaze_powder = "minecraft:blaze_powder"
blaze_rod = "minecraft:blaze_rod"
blitz_powder = "thermalfoundation:material:2051"
blitz_rod = "thermalfoundation:material:2050"
blizz_powder = "thermalfoundation:material:2049"
blizz_rod = "thermalfoundation:material:2048"
blubber = "zawa:blubber"
bone = "minecraft:bone"
bottle_o_enchanting = "minecraft:experience_bottle"
bush_meat = "zawa:bush_meat_raw"
carnivore_meat = "zawa:carnivore_meat_raw"
cetacean_meat = "zawa:cetacean_meat_raw"
cichlid_carcass = "zawa:raw_cichlid"
clownfish_carcass = "minecraft:fish:2"
cow_meat = "minecraft:beef"
crab_carcass = "harvestcraft:crabrawitem"
crab_meat = "zawa:raw_crab_leg"
crocodile_leather = "zawa:crocodile_leather"
crocodile_tooth = "zawa:crocodile_tooth"
diamond = "minecraft:diamond"
duck_meat = "harvestcraft:duckrawitem"
eel_carcass = "harvestcraft:eelrawitem"
elephant_leather = "zawa:elephant_leather"
elephant_tusk = "zawa:ivory_tusk"
emerald = "minecraft:emerald"
ender_pearl = "minecraft:ender_pearl"
feather = "minecraft:feather"
fire_charge = "minecraft:fire_charge"
fish_carcass = "minecraft:fish"
fish_meat = "harvestcraft:groundfishitem"
foliaath_seed = "mowziesmobs:foliaath_seed"
frog_carcass = "harvestcraft:frograwitem"
frog_meat = "zawa:raw_frog_leg"
game_meat = "harvestcraft:venisonrawitem"
generic_fur = "zawa:fur"
generic_leather = "minecraft:leather"
ghast_tear = "minecraft:ghast_tear"
giraffe_fur = "zawa:giraffe_hide"
gorilla_fur = "zawa:gorilla_hide"
gunpowder = "minecraft:gunpowder"
ink_sac = "minecraft:dye"
iron_block = "minecraft:iron_block"
iron_ingot = "minecraft:iron_ingot"
iron_nugget = "minecraft:iron_nugget"
kale = "harvestcraft:kaleitem"
leopard_fur = "zawa:amur_leopard_hide"
luminous_jelly = "mowziesmobs:glowing_jelly"
magma_cream = "minecraft:magma_cream"
mushroom_item = "minecraft:red_mushroom"
naga_fang = "mowziesmobs:naga_fang"
octobus_carcass = "harvestcraft:octopusrawitem"
pangolin_scale = "zawa:pangolin_scale"
pig_meat = "minecraft:porkchop"
pufferfish_carcass = "minecraft:fish:3"
rabbit_carcass = "minecraft:rabbit"
rabbit_foot = "minecraft:rabbit_foot"
rat_carcass = "zawa:rat_raw"
reptile_leather = "zawa:reptile_hide"
reptile_meat = "zawa:reptile_meat_raw"
rhino_leather = "zawa:rhino_hide"
rhino_horn = "zawa:rhino_horn"
ruminant_meat = "zawa:large_meat_raw"
salmon_carcass = "minecraft:fish:1"
sheep_meat = "minecraft:mutton"
slime = "minecraft:slime_ball"
small_fur = "minecraft:rabbit_hide"
snake_skin = "zawa:snakeskin"
spider_eye = "minecraft:spider_eye"
squid_carcass = "harvestcraft:calamarirawitem"
thick_fur = "zawa:thick_fur"
tiger_fur = "zawa:tiger_fur"
tortoise_shell = "zawa:tortoise_shell"
turkey_meat = "harvestcraft:turkeyrawitem"
turtle_carcass = "harvestcraft:turtlerawitem"
venom_sac = "zawa:toxin_sac"
wool = "minecraft:wool"
white_fur = "zawa:polar_bear_hide"
zebra_leather = "zawa:zebra_leather"


# Loot Collections #####################################################################################################

amphibian_small_loot = [Loot("0-1", frog_carcass), Loot("0-1", frog_meat)]
basalz_loot = [Loot("1-3", basalz_rod), Loot("2-4", basalz_powder)]
bird_large_loot = [Loot("1", bird_carcass), Loot("2-4", bird_meat), Loot("2-5", feather)]
bird_medium_loot = [Loot("1", bird_carcass), Loot("0-1", bird_meat), Loot("1-3", feather)]
bird_small_loot = [Loot("1", bird_meat), Loot("0-2", feather)]
blaze_loot = [Loot("1-3", blaze_rod), Loot("2-4", blaze_powder)]
blitz_loot = [Loot("1-3", blitz_rod), Loot("2-4", blitz_powder)]
blizz_loot = [Loot("1-3", blizz_rod), Loot("2-4", blizz_powder)]
cat_large_loot = [Loot("1", generic_fur), Loot("1-2", carnivore_meat), Loot("1-2", bone)]
cat_leopard_loot = [Loot("1", leopard_fur), Loot("1-2", carnivore_meat), Loot("1-2", bone)]
cat_tiger_loot = [Loot("1", tiger_fur), Loot("2-3", carnivore_meat), Loot("2-3", bone)]
cetacean_large_loot = [Loot("4-8", cetacean_meat), Loot("4-8", bone), Loot("3-6", blubber)]
cetacean_medium_loot = [Loot("3-4", cetacean_meat), Loot("3-4", bone), Loot("2-4", blubber)]
cetacean_small_loot = [Loot("2-3", cetacean_meat), Loot("2-3", bone), Loot("1-3", blubber)]
cow_domestic_loot = [Loot("1", generic_leather), Loot("1-2", cow_meat), Loot("1-2", bone)]
cow_fatty_loot = [Loot("1-2", generic_leather), Loot("1-2", blubber), Loot("3-4", ruminant_meat), Loot("3-4", bone)]
cow_fungal_loot = [Loot("1", generic_leather), Loot("1-2", cow_meat), Loot("1-2", bone), Loot("1-3", mushroom_item)]
cow_furry_loot = [Loot("1-2", generic_leather), Loot("1-2", thick_fur), Loot("3-4", ruminant_meat), Loot("3-4", bone)]
crab_loot = [Loot("0-1", crab_carcass), Loot("1-2", crab_meat)]
creeper_loot = [Loot("3-4", gunpowder), Loot("0-1", reptile_leather)]
crocodile_loot = [Loot("3-4", reptile_meat), Loot("2-3", crocodile_leather), Loot("2-3", bone)]
elephant_loot = [
    Loot("3-4", elephant_leather), Loot("4-8", ruminant_meat), Loot("4-8", bone), Loot("1-2", elephant_tusk)
]
enderman_loot = [Loot("1", ender_pearl)]
fish_large_loot = [Loot("1", fish_carcass), Loot("4-8", fish_meat)]
fish_medium_loot = [Loot("1", fish_carcass), Loot("2-4", fish_meat)]
fish_small_loot = [Loot("1", fish_carcass)]
foliaath_loot = [Loot("0-1", foliaath_seed), Loot("3-4", kale)]
frostmaw_loot = [Loot("3-5", white_fur), Loot("5-7", carnivore_meat)]
ghast_loot = [Loot("1-3", ghast_tear), Loot("0-1", fire_charge), Loot("0-2", gunpowder)]
giraffe_loot = [Loot("1-2", giraffe_fur), Loot("4-5", ruminant_meat), Loot("4-5", bone)]
gorilla_loot = [Loot("1-2", bush_meat), Loot("1", gorilla_fur), Loot("1", bone)]
grizzly_bear_loot = [Loot("1-2", thick_fur), Loot("3-4", carnivore_meat)]
horse_loot = [Loot("1", generic_leather), Loot("2-3", game_meat), Loot("1-2", bone)]
horse_zebra_loot = [Loot("1", zebra_leather), Loot("2-3", game_meat), Loot("1-2", bone)]
iron_golem_loot = [Loot("1", iron_block), Loot("1-4", iron_ingot), Loot("0-1", bottle_o_enchanting)]
lantern_loot = [Loot("2-3", luminous_jelly), Loot("0-1", slime)]
llama_loot = [Loot("1-2", wool), Loot("1-2", sheep_meat), Loot("1-2", bone)]
magma_cube_loot = [Loot("1-3", magma_cream)]
mammal_large_loot = [Loot("1-2", bush_meat), Loot("1", generic_fur), Loot("1", bone)]
mammal_medium_loot = [Loot("1", bush_meat), Loot("1", small_fur)]
mammal_small_loot = [Loot("1", rat_carcass)]
naga_loot = [Loot("3-4", reptile_leather), Loot("2-4", naga_fang), Loot("2-4", reptile_meat), Loot("0-1", venom_sac)]
pig_loot = [Loot("2-3", pig_meat), Loot("1-2", bone)]
polar_bear_loot = [Loot("1-2", white_fur), Loot("3-4", carnivore_meat)]
rabbit_loot = [Loot("0-1", rabbit_foot), Loot("1", rabbit_carcass), Loot("1", small_fur)]
reptile_large_loot = [Loot("2-4", reptile_meat), Loot("1-2", reptile_leather), Loot("1-2", bone)]
reptile_medium_loot = [Loot("1-2", reptile_meat), Loot("1", reptile_leather), Loot("1", bone)]
reptile_small_loot = [Loot("1", reptile_meat), Loot("1", reptile_leather)]
reptile_turtle_loot = [Loot("1", turtle_carcass), Loot("1", bone), Loot("0-1", tortoise_shell)]
rhino_loot = [Loot("1-2", rhino_leather), Loot("3-4", ruminant_meat), Loot("3-4", bone), Loot("1", rhino_horn)]
snake_loot = [Loot("3-4", reptile_meat), Loot("1-2", snake_skin)]
spider_loot = [Loot("1-4", spider_eye), Loot("2-6", crab_meat)]
squid_loot = [Loot("1", squid_carcass), Loot("1", ink_sac)]
wolf_loot = [Loot("1", carnivore_meat), Loot("1", bone), Loot("1", generic_fur)]


mammal_venomous_loot = mammal_medium_loot + [Loot("0-1", venom_sac)]
pangolin_loot = mammal_medium_loot + [Loot("2-4", pangolin_scale)]
reptile_venomous_loot = reptile_medium_loot + [Loot("0-1", venom_sac)]
spider_venomous_loot = spider_loot + [Loot("0-1", venom_sac)]


# Animals ##############################################################################################################

albatross = Creature("zawa:albatross", LONER, loot_list=bird_medium_loot)
alligator = Creature("zawa:indiangharial", PAIR, loot_list=crocodile_loot)
anaconda = Creature("zawa:greenanaconda", LONER, loot_list=snake_loot)
baby_foliaath = Creature("mowziesmobs:baby_foliaath", CLUSTER, loot_list=[])
basalz = Creature("thermalfoundation:basalz", CLUSTER, loot_list=basalz_loot)
bat = Creature("minecraft:bat", loot_list=mammal_small_loot)
bear_grizzly = Creature("zawa:grizzlybear", PAIR, loot_list=grizzly_bear_loot)
bear_polar = Creature("zawa:polarbear", LONER, loot_list=polar_bear_loot)
beaver = Creature("zawa:beaver", PAIR, loot_list=mammal_large_loot)
bison = Creature("zawa:americanbison", SWARM, loot_list=cow_furry_loot)
blaze = Creature("minecraft:blaze", CLUSTER, loot_list=blaze_loot)
blitz = Creature("thermalfoundation:blitz", CLUSTER, loot_list=blitz_loot)
blizz = Creature("thermalfoundation:blizz", CLUSTER, loot_list=blizz_loot)
bluefish = Creature("zawa:bluefish", SWARM, loot_list=fish_small_loot)
cassowary = Creature("zawa:cassowary", PAIR, loot_list=bird_large_loot)
cave_spider = Creature("minecraft:cave_spider", LONER, loot_list=spider_venomous_loot)
chicken = Creature("minecraft:chicken", TROOP, loot_list=bird_medium_loot)
chimp = Creature("zawa:commonchimpanzee", TROOP, loot_list=mammal_large_loot)
cichlid = Creature("zawa:cichlid", HERD, loot_list=[Loot("1", cichlid_carcass)])
clownfish = Creature("zawa:clownfish", CLUSTER, loot_list=[Loot("1", clownfish_carcass)])
coatimundi = Creature("zawa:coatimundi", TROOP, loot_list=mammal_medium_loot)
cockatoo = Creature("zawa:cockatoo", TROOP, loot_list=bird_small_loot)
condor = Creature("zawa:andeancondor", PAIR, loot_list=bird_medium_loot)
cow = Creature("minecraft:cow", PAIR, loot_list=cow_domestic_loot)
crab = Creature("zawa:coconutcrab", CLUSTER, loot_list=crab_loot)
creeper = Creature("minecraft:creeper", LONER, loot_list=creeper_loot)
dolphin_ocean = Creature("zawa:bottlenosedolphin", HERD, loot_list=cetacean_small_loot)
dolphin_river = Creature("zawa:amazonriverdolphin", CLUSTER, loot_list=cetacean_small_loot)
donkey = Creature("minecraft:donkey", PAIR, loot_list=horse_loot)
eagle_bald = Creature("zawa:baldeagle", PAIR, loot_list=bird_medium_loot)
eagle_harpy = Creature("zawa:harpyeagle", PAIR, loot_list=bird_large_loot)
echidna = Creature("zawa:echidna", LONER, loot_list=mammal_medium_loot)
eel = Creature("zawa:morayeel", LONER, loot_list=[Loot("1", eel_carcass)])
elephant = Creature("zawa:africanelephant", HERD, loot_list=elephant_loot)
elephant_asian = Creature("zawa:asianelephant", CLUSTER, loot_list=elephant_loot)
enderman = Creature("minecraft:enderman", CLUSTER, loot_list=enderman_loot)
foliaath = Creature("mowziesmobs:foliaath", LONER, loot_list=foliaath_loot)
frigate = Creature("zawa:frigate", TROOP, loot_list=bird_small_loot)
frostmaw = Creature("mowziesmobs:frostmaw", LONER, loot_list=frostmaw_loot)
gaur = Creature("zawa:gaur", HERD, loot_list=cow_furry_loot)
ghast = Creature("minecraft:ghast", LONER, loot_list=ghast_loot)
gilamonster = Creature("zawa:gilamonster", LONER, loot_list=reptile_venomous_loot)
giraffe = Creature("zawa:reticulatedgiraffe", HERD, loot_list=giraffe_loot)
gorilla = Creature("zawa:westernlowlandgorilla", TROOP, loot_list=gorilla_loot)
grottol = Creature("mowziesmobs:grottol", CLUSTER, loot_list=[Loot("1", diamond, diamond, diamond, emerald)])
hippo_nile = Creature("zawa:nilehippopotamus", TROOP, loot_list=cow_fatty_loot)
hippo_pygmy = Creature("zawa:pygmyhippopotamus", PAIR, loot_list=cow_fatty_loot)
horse = Creature("horse_colors:horse_felinoid", HERD, loot_list=horse_loot)
horse_mc = Creature("minecraft:horse", HERD, loot_list=horse_loot)
husk = Creature("minecraft:husk", CLUSTER)
iguana_fiji = Creature("zawa:fijibandediguana", PAIR, loot_list=reptile_small_loot)
iguana_marine = Creature("zawa:marineiguana", PAIR, loot_list=reptile_medium_loot)
iron_golem = Creature("minecraft:villager_golem", LONER, loot_list=iron_golem_loot)
jaguar = Creature("zawa:jaguar", LONER, loot_list=cat_leopard_loot)
kangaroo = Creature("zawa:redkangaroo", TROOP, loot_list=mammal_medium_loot)
koala = Creature("zawa:koala", CLUSTER, loot_list=mammal_medium_loot)
komododragon = Creature("zawa:komododragon", LONER, loot_list=reptile_venomous_loot)
lantern = Creature("mowziesmobs:lantern", CLUSTER, loot_list=lantern_loot)
leopard = Creature("zawa:amurleopard", LONER, loot_list=cat_leopard_loot)
lion = Creature("zawa:africanlion", TROOP, loot_list=cat_large_loot)
llama = Creature("minecraft:llama", HERD, loot_list=llama_loot)
macaw = Creature("zawa:macaw", TROOP, loot_list=bird_small_loot)
magma_cube = Creature("minecraft:magma_cube", TROOP, loot_list=magma_cube_loot)
meerkat = Creature("zawa:meerkat", TROOP, loot_list=mammal_small_loot)
monkey_spider = Creature("zawa:blackspidermonkey", TROOP, loot_list=mammal_medium_loot)
moose = Creature("zawa:moose", PAIR, loot_list=cow_furry_loot)
mooshroom = Creature("minecraft:mooshroom", HERD, loot_list=cow_fungal_loot)
mule = Creature("minecraft:mule", HERD, DAY, loot_list=horse_loot)
naga = Creature("mowziesmobs:naga", PAIR, loot_list=naga_loot)
ocelot = Creature("minecraft:ocelot", LONER, loot_list=cat_leopard_loot)
octopus = Creature("zawa:octopus", LONER, loot_list=[Loot("1", octobus_carcass)])
okapi = Creature("zawa:okapi", CLUSTER, loot_list=horse_loot)
orca = Creature("zawa:orca", CLUSTER, loot_list=cetacean_medium_loot)
owl = Creature("zawa:greathornedowl", LONER, loot_list=bird_medium_loot)
panda_red = Creature("zawa:redpanda", PAIR, loot_list=mammal_medium_loot)
pangolin = Creature("zawa:indianpangolin", CLUSTER, loot_list=pangolin_loot)
parrot = Creature("minecraft:parrot", TROOP, loot_list=bird_small_loot)
pig = Creature("minecraft:pig", PAIR, loot_list=pig_loot)
platypus = Creature("zawa:platypus", PAIR, loot_list=mammal_venomous_loot)
pufferfish = Creature("zawa:pufferfish", CLUSTER, loot_list=[Loot("1", pufferfish_carcass)])
rabbit = Creature("minecraft:rabbit", CLUSTER, loot_list=rabbit_loot)
rat = Creature("zawa:brownrat", TROOP, NIGHT, loot_list=mammal_small_loot)
rattlesnake = Creature("zawa:rattlesnake", LONER, loot_list=reptile_venomous_loot)
rhino_black = Creature("zawa:blackrhinoceros", CLUSTER, loot_list=rhino_loot)
rhino_sumatran = Creature("zawa:sumatranrhinoceros", loot_list=rhino_loot)
salamander = Creature("zawa:japanesegiantsalamander", LONER, loot_list=reptile_medium_loot)
salmon = Creature("zawa:sockeyesalmon", SWARM, loot_list=[Loot("1", salmon_carcass)])
sea_turtle = Creature("zawa:hawksbillseaturtle", CLUSTER, loot_list=reptile_turtle_loot)
shark_great_white = Creature("zawa:greatwhiteshark", LONER, loot_list=fish_large_loot)
shark_tiger = Creature("zawa:tigershark", PAIR, loot_list=fish_medium_loot)
sheep = Creature("minecraft:sheep", HERD)  # don't override loot to allow colored sheep
skeleton = Creature("minecraft:skeleton", PAIR)
skeleton_horse = Creature("minecraft:skeleton_horse", LONER)
slime = Creature("minecraft:slime", CLUSTER)
sloth = Creature("zawa:threetoedsloth", LONER, loot_list=mammal_medium_loot)
snowman = Creature("minecraft:snowman", LONER)
spider = Creature("minecraft:spider", LONER, NIGHT, loot_list=spider_loot)
squid = Creature("minecraft:squid", TROOP, loot_list=squid_loot)
stray = Creature("minecraft:stray", PAIR)
tamarin = Creature("zawa:goldenliontamarin", TROOP, loot_list=mammal_medium_loot)
tang = Creature("zawa:marinetang", HERD, loot_list=fish_small_loot)
tapir = Creature("zawa:braziliantapir", PAIR, loot_list=cow_domestic_loot)
tasmanian_devil = Creature("zawa:tasmaniandevil", PAIR, loot_list=mammal_medium_loot)
tiger = Creature("zawa:bengaltiger", LONER, loot_list=cat_tiger_loot)
tortoise = Creature("zawa:galapagostortoise", CLUSTER, loot_list=reptile_turtle_loot)
toucan = Creature("zawa:toucan", CLUSTER, loot_list=bird_small_loot)
treefrog = Creature("zawa:treefrog", CLUSTER, loot_list=amphibian_small_loot)
walrus = Creature("zawa:pacificwalrus", HERD, loot_list=cetacean_small_loot)
whale_humpback = Creature("zawa:humpbackwhale", CLUSTER, loot_list=cetacean_large_loot)
witch = Creature("minecraft:witch", LONER)
wither_skeleton = Creature("minecraft:wither_skeleton", CLUSTER)
wolf = Creature("minecraft:wolf", TROOP, loot_list=wolf_loot)
zebra = Creature("zawa:grevyszebra", HERD, loot_list=horse_zebra_loot)
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
            with b.light(upper=0):
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
        with b.light(upper=0):
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
            with b.light(upper=0):
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
            with b.light(upper=0):
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
            with b.light(upper=0):
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
