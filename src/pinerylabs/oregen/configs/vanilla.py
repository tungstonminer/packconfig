"""Define a generation schema which matches the vanilla ore generation in Minecraft."""

from pinerylabs.oregen import ConfigFile, Vein
from pinerylabs.oregen.deposits import ClusterDeposit
from pinerylabs.oregen.data import vanilla as mc

########################################################################################################################

config = ConfigFile("00_minecraft.json", priority=1000)
with config as c:

    with c.dimension(mc.overworld):
        with c.biomes(mc.any_biome):
            with c.distribution(mc.anywhere_band):
                c.add(ClusterDeposit(Vein(mc.dirt).with_purity(0.5), 32))
                c.add(ClusterDeposit(Vein(mc.gravel).with_purity(0.4), 32))

            with c.distribution(mc.stone_variants_band):
                c.add(ClusterDeposit(Vein(mc.diorite).with_purity(1.5), 32))
                c.add(ClusterDeposit(Vein(mc.granite).with_purity(1.5), 32))
                c.add(ClusterDeposit(Vein(mc.andesite).with_purity(1.5), 32))

            with c.distribution(mc.coal_band):
                c.add(ClusterDeposit(mc.coal_vein.with_purity(1.0), 16))

            with c.distribution(mc.iron_band):
                c.add(ClusterDeposit(mc.iron_vein.with_purity(1.0), 8))

            with c.distribution(mc.gold_band):
                c.add(ClusterDeposit(mc.gold_vein.with_purity(0.2), 8))

            with c.distribution(mc.lapis_band):
                c.add(ClusterDeposit(mc.lapis_vein.with_purity(0.2), 8))

            with c.distribution(mc.diamond_band):
                c.add(ClusterDeposit(mc.redstone_vein.with_purity(1.5), 8))
                c.add(ClusterDeposit(mc.diamond_vein.with_purity(0.2), 8))

        with c.biomes(mc.mesa_biomes):
            with c.distribution(mc.mesa_band):
                c.add(ClusterDeposit(mc.gold_vein.with_purity(1.3), 8))

        with c.biomes(mc.mountain_biomes):
            with c.distribution(mc.iron_band):
                c.add(ClusterDeposit(mc.silverfish_vein.with_purity(0.4), 9))

            with c.distribution(mc.emerald_band):
                c.add(ClusterDeposit(mc.emerald_vein.with_purity(0.08), 1))

    with c.dimension(mc.nether):
        with c.biomes(mc.nether_biomes):
            with c.distribution(mc.quartz_band):
                c.add(ClusterDeposit(mc.quartz_vein.with_purity(0.8), 16))
