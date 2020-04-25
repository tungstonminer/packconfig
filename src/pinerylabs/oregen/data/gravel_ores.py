"""Define various ores from the GravelOres mod."""

from pinerylabs.oregen import Ore, Vein


# Ores #################################################################################################################

aluminum_gravel_ore = Ore("gravelores:aluminum_gravel_ore")
copper_gravel_ore = Ore("gravelores:copper_gravel_ore")
diamond_gravel_ore = Ore("gravelores:diamond_gravel_ore")
emerald_gravel_ore = Ore("gravelores:emerald_gravel_ore")
gold_gravel_ore = Ore("gravelores:gold_gravel_ore")
iron_gravel_ore = Ore("gravelores:iron_gravel_ore")
lapis_gravel_ore = Ore("gravelores:lapis_gravel_ore")
lead_gravel_ore = Ore("gravelores:lead_gravel_ore")
redstone_gravel_ore = Ore("gravelores:redstone_gravel_ore")
silver_gravel_ore = Ore("gravelores:silver_gravel_ore")
nickel_gravel_ore = Ore("gravelores:nickel_gravel_ore")
tin_gravel_ore = Ore("gravelores:tin_gravel_ore")


# Veins ################################################################################################################

gravel = Ore("minecraft:gravel")

copper_gravel_vein = Vein(copper_gravel_ore, material_ore=gravel)
gold_gravel_vein = Vein(gold_gravel_ore, material_ore=gravel)
iron_gravel_vein = Vein(iron_gravel_ore, material_ore=gravel)
lapis_gravel_vein = Vein(lapis_gravel_ore, material_ore=gravel)
silver_gravel_vein = Vein(silver_gravel_ore, material_ore=gravel)
tin_gravel_vein = Vein(tin_gravel_ore, material_ore=gravel)
