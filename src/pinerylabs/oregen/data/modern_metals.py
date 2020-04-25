"""Define various ores from the ModernMetals mod."""

from pinerylabs.oregen import Ore, Vein


# Ores #################################################################################################################

aluminum_ore = Ore("modernmetals:aluminum_ore")
uranium_ore = Ore("modernmetals:uranium_ore")


# Veins ################################################################################################################

aluminum_vein = Vein(aluminum_ore)
uranium_vein = Vein(uranium_ore)
