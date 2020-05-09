"""Define various ores from the BaseMinerals mod."""

from packconfig.oregen import Ore, Vein


# Ores #################################################################################################################

salt_ore = Ore("baseminerals:salt_ore")
saltpeter_ore = Ore("baseminerals:saltpeter_ore")
sulfur_ore = Ore("baseminerals:sulfur_ore")


# Veins#################################################################################################################

salt_vein = Vein(salt_ore)
saltpeter_vein = Vein(saltpeter_ore)
sulfur_vein = Vein(sulfur_ore)
