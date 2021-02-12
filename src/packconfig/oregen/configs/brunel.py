"""Define a generation schema customized for the Brunel modpack."""

from packconfig.oregen import BiomeSet, ConfigFile, Gradient, Sweep, Vein
from packconfig.oregen.configs import vanilla
from packconfig.oregen.deposits import CaveDeposit, ClusterDeposit
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

desert_nether_band = UniformDistribution("desert_nether", 0, 32)
lava_band = UniformDistribution("lava", 0, 16)
mountain_band = UniformDistribution("mountain", 64, 128)
nether_band = UniformDistribution("nether", 8, 118)
ocean_floor_band = UniformDistribution("ocean_floor", 0, 56)
oil_band = UniformDistribution("oil", 16, 56)
submerged_gravel_band = UniformDistribution("submerged_gravel", 32, 64)


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


# Gradients ############################################################################################################

metal_gradient = Gradient(
    "metal",
    Sweep("max_height", 12, 72), Sweep("min_height", 4, 64),
    Sweep("purity", 2.0, 1.0), Sweep("cluster_size", 8, 1),
)

mountain_gradient = Gradient(
    "mountain",
    Sweep("max_height", 72, 128), Sweep("min_height", 64, 120),
    Sweep("purity", 1.0, 1.5), Sweep("cluster_size", 1, 2),
)

gemstone_gradient = Gradient(
    "gemstone",
    Sweep("max_height", 12, 40), Sweep("min_height", 4, 32),
    Sweep("purity", 0.75, 0.1), Sweep("cluster_size", 2, 1),
)

mineral_buried_gradient = Gradient(
    "buried_mineral",
    Sweep("max_height", 64, 40), Sweep("min_height", 56, 32),
    Sweep("purity", 1.5, 0.25), Sweep("cluster_size", 8, 1),
)

mineral_surface_gradient = Gradient(
    "surface_mineral",
    Sweep("max_height", 72, 128), Sweep("min_height", 64, 120),
    Sweep("purity", 1.25, 0.25), Sweep("cluster_size", 4, 1),
)


# Ores #################################################################################################################

# Filler
gravel = mc.gravel
soul_sand = mc.soul_sand

# Liquids
crude_oil = ip.crude_oil_fluid

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


# Helper Functions #####################################################################################################

def add_biome_standard(config: ConfigFile, metal: Vein, mineral: Vein, gemstone: Vein, rock: Vein):
    if metal is not None:
        c.add(metal_gradient.with_template(ClusterDeposit(metal)))

    if mineral is not None:
        c.add(mineral_buried_gradient.with_template(ClusterDeposit(mineral)))
        c.add(mineral_surface_gradient.with_template(ClusterDeposit(mineral)))

    if gemstone is not None:
        c.add(gemstone_gradient.with_template(ClusterDeposit(gemstone)))

    if rock is not None:
        c.add(ClusterDeposit(rock.with_purity(20), 64))


# Config File ##########################################################################################################

config = ConfigFile("02_brunel.json")
with config as c:
    with c.dimension(mc.overworld):
        with c.biomes(mountain_biomes):
            add_biome_standard(c, Vein(iron_ore), None, Vein(diamond_ore), Vein(marble))
            c.add(mountain_gradient.with_template(ClusterDeposit(Vein(iron_ore))))

            with c.distribution(mountain_band):
                c.add(ClusterDeposit(Vein(iron_gravel_ore, material_ore=gravel, purity=1.0), 2))

        with c.biomes(river_biomes):
            add_biome_standard(c, None, None, None, None)

            with c.distribution(mountain_band):
                c.add(ClusterDeposit(Vein(gold_gravel_ore, material_ore=gravel, purity=0.5), 2))
                c.add(ClusterDeposit(Vein(silver_gravel_ore, material_ore=gravel, purity=1.0), 2))

        with c.biomes(ocean_biomes):
            add_biome_standard(c, None, None, None, Vein(limestone))

            with c.distribution(ocean_floor_band):
                c.add(ClusterDeposit(Vein(iron_gravel_ore, material_ore=gravel, purity=0.8), 1))
                c.add(ClusterDeposit(Vein(copper_gravel_ore, material_ore=gravel, purity=0.7), 1))
                c.add(ClusterDeposit(Vein(tin_gravel_ore, material_ore=gravel, purity=0.6), 1))
                c.add(ClusterDeposit(Vein(nickel_gravel_ore, material_ore=gravel, purity=0.5), 1))
                c.add(ClusterDeposit(Vein(aluminum_gravel_ore, material_ore=gravel, purity=0.4), 1))
                c.add(ClusterDeposit(Vein(lead_gravel_ore, material_ore=gravel, purity=0.3), 1))
                c.add(ClusterDeposit(Vein(silver_gravel_ore, material_ore=gravel, purity=0.2), 1))
                c.add(ClusterDeposit(Vein(gold_gravel_ore, material_ore=gravel, purity=0.1), 1))

        with c.biomes(shore_biomes):
            add_biome_standard(c, None, None, None, Vein(limestone))

        with c.biomes(tundra_biomes):
            add_biome_standard(c, Vein(lead_ore), None, Vein(lapis_ore), Vein(shale))

        with c.biomes(forest_cold_biomes):
            add_biome_standard(c, Vein(nickel_ore), None, None, Vein(diorite))

        with c.biomes(forest_cool_biomes):
            add_biome_standard(c, Vein(uranium_ore), None, None, Vein(gabbro))

        with c.biomes(forest_warm_biomes):
            add_biome_standard(c, Vein(copper_ore), None, None, Vein(andesite))

        with c.biomes(plains_biomes):
            add_biome_standard(c, Vein(tin_ore), Vein(apatite_ore), None, None)

        with c.biomes(swamp_biomes):
            add_biome_standard(c, Vein(silver_ore), Vein(coal_ore), None, Vein(basalt))

        with c.biomes(savanna_biomes):
            add_biome_standard(c, Vein(aluminum_ore), None, Vein(redstone_ore), Vein(granite))

        with c.biomes(forest_hot_biomes):
            add_biome_standard(c, Vein(zinc_ore), None, Vein(emerald_ore), None)

        with c.biomes(mesa_biomes):
            add_biome_standard(c, Vein(gold_ore.weighted(75), stone.weighted(25)), None, None, Vein(granite))

        with c.biomes(desert_biomes):
            g = Gradient(
                "netherrack",
                Sweep("max_height", 8, 32), Sweep("min_height", 0, 26),
                Sweep("purity", 100, 1), Sweep("cluster_size", 32, 1),
            )
            c.add(g.with_template(ClusterDeposit(Vein(netherrack))))

            with c.distribution(desert_nether_band):
                c.add(ClusterDeposit(Vein(quartz_ore, material_ore=netherrack, purity=2.0)))
                c.add(CaveDeposit(Vein(glowstone), cluster_count=4))

        with c.biomes(any_biomes):
            with c.distribution(lava_band):
                c.add(ClusterDeposit(Vein(sulfur_ore).with_purity(0.75), 8))

            with c.distribution(UniformDistribution("monster_band", 0, 24)):
                c.add(ClusterDeposit(mc.silverfish_vein.with_purity(0.5), 2))

    with c.dimension(mc.nether):
        with c.biomes(mc.nether_biomes):
            with c.distribution(nether_band):
                vein = Vein(quartz_ore, material_ore=mc.netherrack, purity=2.0)
                c.add(ClusterDeposit(vein, 12))

    with c.dimension(mc.the_end):
        pass
