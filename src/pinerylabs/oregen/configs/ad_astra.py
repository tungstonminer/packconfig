"""Define a generation schema customized for the Ad Astra modpack."""

from pinerylabs.oregen import BiomeSet, ConfigFile, Gradient, Quantity, Sweep, Vein
from pinerylabs.oregen.configs import vanilla
from pinerylabs.oregen.deposits import BoulderDeposit, ClusterDeposit, GeodeDeposit, LakeDeposit, PlateDeposit
from pinerylabs.oregen.distributions import NormalDistribution, SurfaceDistribution, UniformDistribution
from pinerylabs.oregen.data import (
    advanced_rocketry as ar,
    chisel as ch,
    extreme_reactors as er,
    gravel_ores as go,
    railcraft as rc,
    thermal_foundation as tf,
    vanilla as mc,
)

__all__ = []


########################################################################################################################

# Ores from the bronze age are readily available near the surface at low purity.  Those ores available anywhere include:
#
#     copper    stone ore, gravel ore
#     zinc      stone ore
#     tin       stone ore, gravel ore
#     iron      tiny boulders (very rare in desert), gravel ore (common, but very low purity)
#     lapis     gravel ore (moderately rare, rivers only)
#
#
# Ore from the iron age and later, only appears in specific biomes, and the bronze age metals appear in greater
# concentration.  Each of these biomes has a gradient of ore from the depths to the mountain tops where the
# concentration is greater the further away from sea level one goes. These deposits are randomly scattered clusters of
# ore which grow in size as the purity increases.  It should be fairly trivial to pick up a few pieces of ore from
# surface caves, but impossible to get a whole stack. For a mine nearly at the lava level, it should be fairly easy to
# pick up a stack.  The following chart shows the biome distribution:
#
#     aluminum                    plains biomes
#     copper / zinc / tin         forest biomes
#     iron / nickel / platinum    mountain biomes
#     lead / uranium / monatize   tundra biomes
#     gold / silver               mesa biomes
#
#
# Mineral deposits are handled differently.  Coal is found in a gradient of increasing purity from the surface to the
# lava layer under the massively overgrown biomes (e.g., jungle, redwood taiga, swamp, etc.).  Gemstones form alongside
# coal in the lava layer.  Sulfur is found distributed throughout the lava layer in all biomes.
#
#     coal        redwood / jungle / swamp
#     diamonds    under coal in redwood
#     emeralds    under coal in swamp
#     redstone    under coal in jungle
#     sulfur      all at LAVA layer
#
#
# Oceans are a little different still, in that they contain a blend of low-purity ores of all types, including in the
# gravel layer on the ocean floor.  Finally, salt is found under beaches and shore biomes near the surface.


# Overrides ############################################################################################################

vanilla.config.enabled = False


# Distributions ########################################################################################################

above_ground_band = UniformDistribution("above_ground", 65, 138)
bedrock_band = UniformDistribution("bedrock", 0, 5)
below_ground_band = UniformDistribution("below_ground", 0, 64)
lava_band = UniformDistribution("lava", 0, 16)
nether_band = UniformDistribution("nether", 8, 118)
ocean_floor_band = UniformDistribution("ocean_floor", 0, 40)
oil_band = UniformDistribution("oil", 16, 56)
submerged_gravel_band = UniformDistribution("submerged_gravel", 32, 64)
surface_band = NormalDistribution("surface", 64, 16)
on_surface = SurfaceDistribution("surface_feature")


# Biomes ###############################################################################################################

any_biomes = BiomeSet.ANY
diamond_biomes = BiomeSet().add(mc.roofed_forest_biomes)
emerald_biomes = BiomeSet().add(mc.swamp_biomes)
redstone_biomes = BiomeSet().add(mc.jungle_biomes)

desert_biomes = BiomeSet().add(mc.desert_biomes)
forest_cold_biomes = BiomeSet().add(mc.redwood_forest_biomes, mc.spruce_forest_biomes)
forest_hot_biomes = BiomeSet().add(mc.jungle_biomes)
forest_warm_biomes = BiomeSet().add(mc.birch_forest_biomes, mc.oak_forest_biomes, mc.roofed_forest_biomes)
mesa_biomes = BiomeSet().add(mc.mesa_biomes)
mountain_biomes = BiomeSet().add(mc.mountain_biomes).remove(mc.tundra_biomes)
ocean_biomes = BiomeSet().add(mc.ocean_biomes)
plains_biomes = BiomeSet().add(mc.plains_biomes)
river_biomes = BiomeSet().add(mc.river_biomes)
savanna_biomes = BiomeSet().add(mc.savanna_biomes)
shore_biomes = BiomeSet().add(mc.shore_biomes)
swamp_biomes = BiomeSet().add(mc.swamp_biomes)
tundra_biomes = BiomeSet().add(mc.tundra_biomes)


# Gradients ############################################################################################################

surface_down = Gradient(
    "surface_down",
    Sweep("max_height", 80, 48), Sweep("min_height", 72, 40),
    Sweep("purity", 1.0, 0.25), Sweep("cluster_size", 2, 1),
)

deep_up = Gradient(
    "deep_up",
    Sweep("max_height", 16, 48), Sweep("min_height", 8, 40),
    Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
)

surface_up = Gradient(
    "surface_up",
    Sweep("max_height", 80, 128), Sweep("min_height", 72, 120),
    Sweep("purity", 1.0, 1.5), Sweep("cluster_size", 2, 1),
)


# Ores #################################################################################################################

# Clathrates
endstone_clathrate = tf.resonant_end_stone
glowstone_clathrate = tf.energized_netherrack
gravel_oil_clathrate = tf.gravel_oil_ore
red_sand_oil_clathrate = tf.red_sand_oil_ore
redstone_clathrate = tf.destabilized_redstone
sand_oil_clathrate = tf.sand_oil_ore

# Liquids
crude_oil = tf.crude_oil_fluid
ender_fluid = tf.ender_fluid
glowstone_fluid = tf.glowstone_fluid
lava = mc.lava
redstone_fluid = tf.redstone_fluid
water = mc.water

# Metals
aluminum_ore = ar.aluminum_ore
aluminum_gravel_ore = go.aluminum_gravel_ore
copper_ore = rc.copper_ore
copper_gravel_ore = go.copper_gravel_ore
copper_poor_ore = rc.copper_poor_ore
gold_ore = mc.gold_ore
gold_gravel_ore = go.gold_gravel_ore
gold_poor_ore = rc.gold_poor_ore
iridium_ore = ar.iridium_ore
iron_ore = mc.iron_ore
iron_gravel_ore = go.iron_gravel_ore
iron_poor_ore = rc.iron_poor_ore
lead_ore = rc.lead_ore
lead_gravel_ore = go.lead_gravel_ore
lead_poor_ore = rc.lead_poor_ore
nickel_ore = rc.nickel_ore
nickel_gravel_ore = go.nickel_gravel_ore
nickel_poor_ore = rc.nickel_poor_ore
platinum_ore = tf.platinum_ore
silver_ore = rc.silver_ore
silver_gravel_ore = go.silver_gravel_ore
silver_poor_ore = rc.silver_poor_ore
tin_ore = rc.tin_ore
tin_gravel_ore = go.tin_gravel_ore
tin_poor_ore = rc.tin_poor_ore
titanium_ore = ar.titanium_ore
uranium_ore = er.yellorite_ore
zinc_ore = rc.zinc_ore
zinc_poor_ore = rc.zinc_poor_ore

# Minerals
coal_ore = mc.coal_ore
dilithium_ore = ar.dilithium_ore
diamond_ore = mc.diamond_ore
diamond_dark_ore = rc.diamond_dark_ore
emerald_ore = mc.emerald_ore
emerald_dark_ore = rc.emerald_dark_ore
lapis_ore = mc.lapis_ore
lapis_dark_ore = rc.lapis_dark_ore
lapis_gravel_ore = go.lapis_gravel_ore
quartz_ore = mc.quartz_ore
redstone_ore = mc.redstone_ore
saltpeter_ore = rc.saltpeter_ore
sulfur_ore = rc.sulfur_ore

# Stones
andesite = mc.andesite
basalt = ch.basalt
diorite = mc.diorite
endstone = mc.endstone
gabbro = rc.abyssal_stone
granite = mc.granite
gravel = mc.gravel
limestone = ch.limestone
marble = ch.marble
obsidian = mc.obsidian
shale = rc.quaried_stone
stone = mc.stone


# Config File ##########################################################################################################

config = ConfigFile("04_ad_astra.json")
with config as c:
    with c.dimension(mc.overworld):
        with c.biomes(desert_biomes):
            with c.distribution(bedrock_band):
                c.add(PlateDeposit(Vein(rc.saltpeter_spawner, material_ore=mc.bedrock, purity=10)))

            with c.distribution(surface_band):
                c.add(PlateDeposit(Vein(sand_oil_clathrate, material_ore=mc.sand, purity=25), percent=20))

            with c.distribution(below_ground_band):
                c.add(LakeDeposit(Vein(mc.stone), crude_oil, 32, percent=25))

        with c.biomes(forest_cold_biomes):
            rich_vein = Vein(
                nickel_ore.weighted(75),
                iron_ore.weighted(20),
                platinum_ore.weighted(4),
                iridium_ore.weighted(1)
            )
            poor_vein = Vein(
                nickel_poor_ore.weighted(55),
                iron_poor_ore.weighted(20),
                nickel_ore.weighted(15),
                iron_ore.weighted(5),
            )

            c.add(ClusterDeposit(Vein(andesite).with_purity(10), 64))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(forest_hot_biomes):
            rich_vein = Vein(
                aluminum_ore.weighted(60),
                zinc_ore.weighted(20),
                stone.weighted(10),
                zinc_poor_ore.weighted(5),
            )
            poor_vein = Vein(
                stone.weighted(43),
                zinc_poor_ore.weighted(20),
                aluminum_ore.weighted(32),
                zinc_ore.weighted(5),
            )

            with c.distribution(UniformDistribution("shallow", 40, 64)):
                c.add(PlateDeposit(Vein(limestone).with_purity(100), 4, 24, percent=20))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(forest_warm_biomes):
            rich_vein = Vein(
                copper_ore.weighted(75),
                copper_poor_ore.weighted(15),
                gold_poor_ore.weighted(9),
                gold_ore.weighted(1),
            )
            poor_vein = Vein(
                copper_poor_ore.weighted(75),
                copper_ore.weighted(20),
                gold_poor_ore.weighted(5),
            )

            with c.distribution(lava_band):
                c.add(LakeDeposit(Vein(emerald_ore).with_purity(10), lava, 16, percent=33))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(mesa_biomes):
            rich_vein = Vein(
                stone.weighted(34),
                silver_poor_ore.weighted(23),
                silver_ore.weighted(10),
                gold_poor_ore.weighted(23),
                gold_ore.weighted(10),
            )
            poor_vein = Vein(
                stone.weighted(50),
                silver_poor_ore.weighted(25),
                gold_poor_ore.weighted(25),
            )

            with c.distribution(surface_band):
                c.add(PlateDeposit(Vein(red_sand_oil_clathrate, material_ore=mc.red_sand, purity=25), percent=33))

            with c.distribution(below_ground_band):
                c.add(LakeDeposit(Vein(mc.stone), crude_oil, 32, percent=10))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(ar.moon_biomes):
            rich_vein = Vein(
                aluminum_ore.weighted(45),
                iron_ore.weighted(35),
                titanium_ore.weighted(20),
            )

            with c.distribution(UniformDistribution("lunar_hills", 68, 100)):
                c.add(PlateDeposit(Vein(mc.ice), 8, 32, cluster_count=0.25, percent=5))

            with c.distribution(UniformDistribution("lunar_deeps", 16, 24)):
                c.add(ClusterDeposit(Vein(dilithium_ore).with_purity(1.0), 2))

            c.add(ClusterDeposit(rich_vein.with_purity(4.0), 12))

        with c.biomes(ar.mars_biomes):
            rich_vein = Vein(
                iron_ore.weighted(45),
                aluminum_ore.weighted(30),
                titanium_ore.weighted(15),
                iridium_ore.weighted(10)
            )
            replaces = [mc.stone, ar.basalt]

            c.add(ClusterDeposit(Vein(basalt).with_purity(20), 16, replaces=replaces))
            c.add(ClusterDeposit(rich_vein.with_purity(4.0), 12, replaces=replaces))

        with c.biomes(ar.volcanic_biomes):
            rich_vein = Vein(
                aluminum_ore.weighted(8),
                nickel_ore.weighted(5),
                iron_ore.weighted(3),
                gold_ore.weighted(2),
                diamond_ore.weighted(1),
            )
            replaces = [mc.stone, ar.basalt]

            c.add(ClusterDeposit(rich_vein.with_purity(5.0), 4, replaces=replaces))
            c.add(ClusterDeposit(Vein(mc.obsidian).with_purity(2.0), 12, replaces=replaces))

        with c.biomes(mountain_biomes):
            rich_vein = Vein(
                iron_ore.weighted(65),
                iron_poor_ore.weighted(10),
                nickel_ore.weighted(15),
                nickel_poor_ore.weighted(10),
            )
            poor_vein = Vein(
                iron_poor_ore.weighted(65),
                iron_ore.weighted(10),
                nickel_poor_ore.weighted(15),
                nickel_ore.weighted(10),
            )
            gravel_vein = Vein(iron_gravel_ore, material_ore=gravel).with_purity(20)

            with c.distribution(above_ground_band):
                c.add(PlateDeposit(Vein(marble).with_purity(100), 4, 16, percent=20))
                c.add(PlateDeposit(gravel_vein, 2, 8))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(ocean_biomes):
            gabbro_vein = Vein(
                gabbro.weighted(94),
                diamond_dark_ore.weighted(2),
                emerald_dark_ore.weighted(2),
                lapis_dark_ore.weighted(2),
            )
            gravel_vein = Vein(
                aluminum_gravel_ore.weighted(33),
                iron_gravel_ore.weighted(21),
                nickel_gravel_ore.weighted(13),
                copper_gravel_ore.weighted(8),
                lead_gravel_ore.weighted(5),
                tin_gravel_ore.weighted(3),
                silver_gravel_ore.weighted(2),
                gold_gravel_ore.weighted(1),
                material_ore=mc.gravel,
            )
            poor_vein = Vein(
                iron_poor_ore.weighted(33),
                nickel_poor_ore.weighted(21),
                zinc_poor_ore.weighted(13),
                copper_poor_ore.weighted(8),
                lead_poor_ore.weighted(5),
                tin_poor_ore.weighted(3),
                silver_poor_ore.weighted(2),
                gold_poor_ore.weighted(1),
            )

            with c.distribution(ocean_floor_band):
                c.add(ClusterDeposit(poor_vein.with_purity(0.5), 1))

            with c.distribution(submerged_gravel_band):
                c.add(PlateDeposit(gravel_vein.with_purity(15), percent=100))

            with c.distribution(lava_band):
                c.add(ClusterDeposit(Vein(sulfur_ore, purity=2.0), 8))

        with c.biomes(BiomeSet("minecraft:deep_ocean")):
            with c.distribution(ocean_floor_band):
                c.add(GeodeDeposit(gabbro_vein, Vein(mc.air))),

        with c.biomes(plains_biomes):
            rich_vein = Vein(
                tin_ore.weighted(55),
                zinc_ore.weighted(20),
                tin_poor_ore.weighted(15),
                zinc_poor_ore.weighted(5),
            )
            poor_vein = Vein(
                tin_poor_ore.weighted(55),
                zinc_poor_ore.weighted(20),
                tin_ore.weighted(15),
                zinc_ore.weighted(5),
            )

            with c.distribution(UniformDistribution("deep", 16, 40)):
                c.add(PlateDeposit(Vein(diorite).with_purity(100), 4, 24, percent=20))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(river_biomes):
            gravel_vein = Vein(
                lapis_gravel_ore.weighted(50),
                silver_gravel_ore.weighted(35),
                gold_gravel_ore.weighted(15),
                material_ore=mc.gravel,
            )
            stone_vein = Vein(
                lapis_ore.weighted(50),
                silver_poor_ore.weighted(35),
                gold_poor_ore.weighted(15),
            )

            with c.distribution(submerged_gravel_band):
                c.add(ClusterDeposit(gravel_vein.with_purity(2.0), 2, percent=100))

            c.add(surface_down.with_template(ClusterDeposit(stone_vein)))

        with c.biomes(savanna_biomes):
            rich_vein = Vein(
                copper_poor_ore.weighted(30),
                tin_poor_ore.weighted(30),
                copper_ore.weighted(20),
                tin_ore.weighted(20),
            )
            poor_vein = Vein(
                copper_poor_ore.weighted(50),
                tin_poor_ore.weighted(50),
            )
            geode_vein = Vein(redstone_clathrate, material_ore=gravel)
            granite_vein = Vein(granite)

            with c.distribution(on_surface):
                c.add(BoulderDeposit(granite_vein.with_purity(100), Quantity(1, 2), 1, percent=25))

            c.add(ClusterDeposit(granite_vein.with_purity(10), 16))

            with c.distribution(UniformDistribution("deep", 16, 40)):
                c.add(GeodeDeposit(geode_vein.with_purity(10), redstone_fluid))

            with c.distribution(lava_band):
                c.add(ClusterDeposit(Vein(redstone_ore).with_purity(1.5), 8))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(shore_biomes):
            with c.distribution(surface_band):
                c.add(ClusterDeposit(Vein(titanium_ore).with_purity(2.0), 4))

        with c.biomes(swamp_biomes):
            coal_vein = Vein(
                coal_ore.weighted(99.5),
                diamond_ore.weighted(0.5),
            )
            coal_gradient = Gradient(
                "coal_gradient",
                Sweep("max_height", 60, 8), Sweep("min_height", 52, 0),
                Sweep("purity", 3.0, 0.25), Sweep("cluster_size", 12, 1),
            )

            with c.distribution(lava_band):
                c.add(LakeDeposit(Vein(diamond_ore).with_purity(10), lava, 16, percent=33))

            with c.distribution(lava_band):
                c.add(PlateDeposit(Vein(basalt).with_purity(100), 4, 16, percent=20))

            c.add(coal_gradient.with_template(ClusterDeposit(coal_vein)))

        with c.biomes(tundra_biomes):
            rich_vein = Vein(
                lead_ore.weighted(50),
                uranium_ore.weighted(25),
                silver_poor_ore.weighted(15),
                silver_ore.weighted(10),
            )
            poor_vein = Vein(
                lead_poor_ore.weighted(40),
                silver_poor_ore.weighted(30),
                lead_ore.weighted(15),
                silver_ore.weighted(10),
                uranium_ore.weighted(5),
            )

            with c.distribution(surface_band):
                c.add(PlateDeposit(Vein(gravel_oil_clathrate, material_ore=gravel, purity=25), percent=33))

            with c.distribution(below_ground_band):
                c.add(LakeDeposit(Vein(mc.stone), crude_oil, 32, percent=10))

            c.add(PlateDeposit(Vein(shale).with_purity(100), 4, 24, percent=20))

            c.add(deep_up.with_template(ClusterDeposit(rich_vein)))
            c.add(surface_down.with_template(ClusterDeposit(poor_vein)))
            c.add(surface_up.with_template(ClusterDeposit(poor_vein)))

        with c.biomes(BiomeSet.ANY):
            with c.distribution(UniformDistribution("monster_band", 0, 24)):
                c.add(ClusterDeposit(mc.silverfish_vein.with_purity(0.5), 2))

    with c.dimension(mc.nether):
        with c.biomes(mc.nether_biomes):
            with c.distribution(UniformDistribution("nether_floor", 24, 40)):
                replaces = [mc.air, mc.netherrack, mc.magma, mc.lava]
                lake_vein = Vein(glowstone_clathrate, material_ore=mc.netherrack).with_purity(25)
                c.add(GeodeDeposit(lake_vein, Vein(glowstone_fluid), replaces=replaces, percent=5)),

            with c.distribution(nether_band):
                c.add(ClusterDeposit(Vein(quartz_ore, material_ore=mc.netherrack).with_purity(1.0), 12))

    with c.dimension(mc.the_end):
        with c.biomes(mc.the_end_biomes):
            c.add(LakeDeposit(Vein(endstone_clathrate, endstone), ender_fluid, 4, percent=1, replaces=endstone))
