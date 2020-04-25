"""Define various ores from the Chisel mod."""

from pinerylabs.oregen import Ore, Vein


# Ores #################################################################################################################

basalt = Ore("chisel:basalt2", 7)
limestone = Ore("chisel:limestone2", 7)
marble = Ore("chisel:marble2", 7)

# Veins#################################################################################################################

basalt_vein = Vein(basalt)
limestone_vein = Vein(limestone)
marble_vein = Vein(marble)
