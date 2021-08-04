"""Define a generation schema customized for the Brunel modpack."""

from packconfig.oregen import BiomeSet, ConfigFile, Gradient, Sweep, Vein
from packconfig.oregen.configs import vanilla
from packconfig.oregen.deposits import CaveDeposit, ClusterDeposit, LakeDeposit
from packconfig.oregen.distributions import UniformDistribution
from packconfig.oregen.data import (
    chisel as ch,
    forestry as fo,
    gravel_ores as go,
    immersive_engineering as im,
    immersive_petrolium as ip,
    railcraft as rc,
    vanilla as mc,
)

__all__ = []


# Overrides ############################################################################################################

vanilla.config.enabled = False


# Distributions ########################################################################################################

deep_band = UniformDistribution("deep", 16, 48)
lava_band = UniformDistribution("lava", 0, 16)
mountain_band = UniformDistribution("mountain", 64, 128)
nether_band = UniformDistribution("nether", 8, 118)
ocean_floor_band = UniformDistribution("ocean_floor", 0, 56)
submerged_gravel_band = UniformDistribution("submerged_gravel", 32, 64)
surface_band = UniformDistribution("surface", 48, 80)


# Biomes ###############################################################################################################

any_biomes = BiomeSet.ANY

desert_biomes = BiomeSet().add(mc.desert_biomes)
forest_cold_biomes = BiomeSet().add(mc.redwood_forest_biomes, mc.spruce_forest_biomes)
forest_cool_biomes = BiomeSet().add(mc.roofed_forest_biomes)
forest_hot_biomes = BiomeSet().add(mc.jungle_biomes)
forest_warm_biomes = BiomeSet().add(mc.birch_forest_biomes, mc.oak_forest_biomes)
mesa_biomes = BiomeSet().add(mc.mesa_biomes)
mountain_biomes = BiomeSet().add(mc.mountain_biomes).remove(mc.tundra_biomes)
ocean_biomes = BiomeSet().add(mc.ocean_biomes)
plains_biomes = BiomeSet().add(mc.plains_biomes)
river_biomes = BiomeSet().add(mc.river_biomes)
savanna_biomes = BiomeSet().add(mc.savanna_biomes)
shore_biomes = BiomeSet().add(mc.shore_biomes)
swamp_biomes = BiomeSet().add(mc.swamp_biomes)
tundra_biomes = BiomeSet().add(mc.tundra_biomes)


# Ores #################################################################################################################

# Filler
gravel = mc.gravel
soul_sand = mc.soul_sand

# Liquids
crude_oil = ip.crude_oil_fluid
lava = mc.lava

# Metals
aluminum_ore = im.aluminum_ore
copper_ore = im.copper_ore
gold_ore = mc.gold_ore
iron_ore = mc.iron_ore
lead_ore = im.lead_ore
nickel_ore = im.nickel_ore
silver_ore = im.silver_ore
tin_ore = fo.tin_ore
uranium_ore = im.uranium_ore
zinc_ore = rc.zinc_ore

gold_gravel_ore = go.gold_gravel_ore
iron_gravel_ore = go.iron_gravel_ore
silver_gravel_ore = go.silver_gravel_ore
aluminum_gravel_ore = go.aluminum_gravel_ore
copper_gravel_ore = go.copper_gravel_ore
lead_gravel_ore = go.lead_gravel_ore
nickel_gravel_ore = go.nickel_gravel_ore
tin_gravel_ore = go.tin_gravel_ore

# Minerals
apatite_ore = fo.apatite_ore
coal_ore = mc.coal_ore
diamond_ore = mc.diamond_ore
emerald_ore = mc.emerald_ore
glowstone = mc.glowstone
lapis_ore = mc.lapis_ore
lapis_gravel_ore = go.lapis_gravel_ore
quartz_ore = mc.quartz_ore
redstone_ore = mc.redstone_ore
sulfur_ore = rc.sulfur_ore

# Stones
andesite = mc.andesite
basalt = ch.basalt
diorite = mc.diorite
endstone = mc.endstone
gabbro = rc.abyssal_stone
granite = mc.granite
limestone = ch.limestone
marble = ch.marble
netherrack = mc.netherrack
obsidian = mc.obsidian
shale = rc.quaried_stone
stone = mc.stone


# Config File ##########################################################################################################

config = ConfigFile("02_brunel.json")
with config as c:
    with c.dimension(mc.overworld):
        with c.biomes(mountain_biomes):
            g = Gradient(
                "buried_iron",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(iron_ore))))

            g = Gradient(
                "mountain_iron",
                Sweep("max_height", 72, 128), Sweep("min_height", 64, 120),
                Sweep("purity", 1.0, 1.5), Sweep("cluster_size", 1, 2),
            )
            c.add(g.with_template(ClusterDeposit(Vein(iron_ore))))

            g = Gradient(
                "mountain_lapis",
                Sweep("max_height", 104, 256), Sweep("min_height", 96, 248),
                Sweep("purity", 1.0, 1.5), Sweep("cluster_size", 2, 4),
            )
            c.add(g.with_template(ClusterDeposit(Vein(lapis_ore))))

            with c.distribution(mountain_band):
                c.add(ClusterDeposit(Vein(marble).with_purity(15), 32))
                c.add(ClusterDeposit(Vein(iron_gravel_ore, material_ore=gravel, purity=1.0), 2))

        with c.biomes(river_biomes):
            with c.distribution(submerged_gravel_band):
                c.add(ClusterDeposit(Vein(iron_gravel_ore, material_ore=gravel, purity=1.0), 2))
                c.add(ClusterDeposit(Vein(silver_gravel_ore, material_ore=gravel, purity=0.5), 2))
                c.add(ClusterDeposit(Vein(gold_gravel_ore, material_ore=gravel, purity=0.25), 2))

        with c.biomes(ocean_biomes):
            with c.distribution(ocean_floor_band):
                c.add(ClusterDeposit(Vein(limestone).with_purity(15), 32))
                c.add(ClusterDeposit(Vein(iron_gravel_ore, material_ore=gravel, purity=0.8), 1))
                c.add(ClusterDeposit(Vein(copper_gravel_ore, material_ore=gravel, purity=0.7), 1))
                c.add(ClusterDeposit(Vein(tin_gravel_ore, material_ore=gravel, purity=0.6), 1))
                c.add(ClusterDeposit(Vein(nickel_gravel_ore, material_ore=gravel, purity=0.5), 1))
                c.add(ClusterDeposit(Vein(aluminum_gravel_ore, material_ore=gravel, purity=0.4), 1))
                c.add(ClusterDeposit(Vein(lead_gravel_ore, material_ore=gravel, purity=0.3), 1))
                c.add(ClusterDeposit(Vein(silver_gravel_ore, material_ore=gravel, purity=0.2), 1))
                c.add(ClusterDeposit(Vein(gold_gravel_ore, material_ore=gravel, purity=0.1), 1))

        with c.biomes(shore_biomes):
            with c.distribution(ocean_floor_band):
                c.add(ClusterDeposit(Vein(limestone).with_purity(15), 32))

        with c.biomes(tundra_biomes):
            g = Gradient(
                "buried_galena",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(lead_ore.weighted(75), silver_ore.weighted(25)))))

            with c.distribution(surface_band):
                c.add(ClusterDeposit(Vein(shale).with_purity(15), 32))

        with c.biomes(forest_cold_biomes):
            g = Gradient(
                "buried_nickel",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(nickel_ore))))

            with c.distribution(deep_band):
                c.add(ClusterDeposit(Vein(diorite).with_purity(15), 32))

        with c.biomes(forest_cool_biomes):
            g = Gradient(
                "buried_uranium",
                Sweep("max_height", 12, 40), Sweep("min_height", 4, 32),
                Sweep("purity", 1.5, 0.5), Sweep("cluster_size", 8, 4),
            )
            v = Vein(lead_ore.weighted(75), uranium_ore.weighted(25))
            c.add(g.with_template(ClusterDeposit(v)))

            with c.distribution(deep_band):
                c.add(ClusterDeposit(Vein(gabbro).with_purity(15), 32))

        with c.biomes(forest_warm_biomes):
            g = Gradient(
                "buried_copper",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 1.0, 2.0), Sweep("cluster_size", 1, 8),
            )
            v = Vein(copper_ore.weighted(90), redstone_ore.weighted(10))
            c.add(g.with_template(ClusterDeposit(v)))

            g = Gradient(
                "buried_redstone",
                Sweep("max_height", 8, 12), Sweep("min_height", 0, 16),
                Sweep("purity", 2.0, 0.5), Sweep("cluster_size", 8, 1),
            )
            v = Vein(redstone_ore.weighted(75), copper_ore.weighted(25))
            c.add(g.with_template(ClusterDeposit(v)))

            with c.distribution(deep_band):
                c.add(ClusterDeposit(Vein(andesite).with_purity(15), 32))

        with c.biomes(plains_biomes):
            g = Gradient(
                "buried_tin",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 1.0, 2.0), Sweep("cluster_size", 1, 8),
            )
            v = Vein(tin_ore.weighted(80), zinc_ore.weighted(20))
            c.add(g.with_template(ClusterDeposit(v)))

            with c.distribution(deep_band):
                c.add(ClusterDeposit(Vein(andesite).with_purity(15), 32))

        with c.biomes(swamp_biomes):
            coal_vein = Vein(
                coal_ore.weighted(99),
                diamond_ore.weighted(1),
            )
            coal_gradient = Gradient(
                "coal_gradient",
                Sweep("max_height", 60, 8), Sweep("min_height", 52, 0),
                Sweep("purity", 4.0, 0.5), Sweep("cluster_size", 12, 1),
            )

            with c.distribution(lava_band):
                c.add(ClusterDeposit(Vein(diamond_ore).with_purity(0.5), 2))

            c.add(coal_gradient.with_template(ClusterDeposit(coal_vein)))
            c.add(ClusterDeposit(Vein(basalt).with_purity(15), 32))

        with c.biomes(savanna_biomes):
            g = Gradient(
                "buried_aluminum",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 2.0, 0.5), Sweep("cluster_size", 8, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(aluminum_ore))))

            with c.distribution(deep_band):
                c.add(ClusterDeposit(Vein(granite).with_purity(15), 32))

        with c.biomes(forest_hot_biomes):
            g = Gradient(
                "buried_apatite",
                Sweep("max_height", 54, 80), Sweep("min_height", 48, 72),
                Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(apatite_ore))))

            with c.distribution(lava_band):
                c.add(ClusterDeposit(Vein(emerald_ore).with_purity(0.5), 2))

        with c.biomes(mesa_biomes):
            g = Gradient(
                "buried_gold",
                Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
                Sweep("purity", 0.5, 0.25), Sweep("cluster_size", 4, 2),
            )
            c.add(g.with_template(ClusterDeposit(Vein(gold_ore))))

            g = Gradient(
                "mesa_gold",
                Sweep("max_height", 72, 128), Sweep("min_height", 64, 120),
                Sweep("purity", 0.25, 0.1), Sweep("cluster_size", 2, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(gold_ore))))

        with c.biomes(desert_biomes):
            g = Gradient(
                "netherrack",
                Sweep("max_height", 8, 48), Sweep("min_height", 0, 32),
                Sweep("purity", 100, 1), Sweep("cluster_size", 32, 1),
            )
            vein = Vein(netherrack.weighted(999), mc.lava.weighted(1))
            c.add(g.with_template(ClusterDeposit(vein)))

            with c.distribution(UniformDistribution("oil", 48, 60)):
                c.add(LakeDeposit(Vein(coal_ore).with_purity(10), crude_oil, 64, deposit_name="crude_oil", percent=25))

            with c.distribution(UniformDistribution("desert_nether", 0, 48)):
                c.add(ClusterDeposit(Vein(quartz_ore, material_ore=netherrack, purity=2.0)))
                c.add(CaveDeposit(Vein(glowstone), cluster_count=16, max_elevation=48))
                c.add(CaveDeposit(Vein(soul_sand), ceiling=False, cluster_count=16, max_elevation=48))

        with c.biomes(any_biomes):
            with c.distribution(lava_band):
                c.add(LakeDeposit(Vein(sulfur_ore).with_purity(10), lava, 16, percent=33))

            with c.distribution(UniformDistribution("monster_band", 0, 24)):
                c.add(ClusterDeposit(mc.silverfish_vein.with_purity(0.5), 2))

    with c.dimension(mc.nether):
        with c.biomes(mc.nether_biomes):
            with c.distribution(nether_band):
                vein = Vein(quartz_ore, material_ore=mc.netherrack, purity=2.0)
                c.add(ClusterDeposit(vein, 12))

    with c.dimension(mc.the_end):
        pass
