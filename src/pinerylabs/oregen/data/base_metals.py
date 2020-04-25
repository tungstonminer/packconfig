"""Define various ores from the BaseMetals mod."""

from pinerylabs.oregen import Ore, Vein


# Ores #################################################################################################################

copper_ore = Ore("basemetals:copper_ore")
lead_ore = Ore("basemetals:lead_ore")
nickel_ore = Ore("basemetals:nickel_ore")
platinum_ore = Ore("basemetals:platinum_ore")
silver_ore = Ore("basemetals:silver_ore")
tin_ore = Ore("basemetals:tin_ore")
zinc_ore = Ore("basemetals:zinc_ore")


# Veins ################################################################################################################

copper_vein = Vein(copper_ore)
lead_vein = Vein(lead_ore)
nickel_vein = Vein(nickel_ore)
platinum_vein = Vein(platinum_ore)
silver_vein = Vein(silver_ore)
tin_vein = Vein(tin_ore)
zinc_vein = Vein(zinc_ore)
