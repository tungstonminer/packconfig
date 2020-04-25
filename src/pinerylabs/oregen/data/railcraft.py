"""Define various ores from the Chisel mod."""

from pinerylabs.oregen import Ore, Vein


# Ores #################################################################################################################

# Metals
copper_ore = Ore("railcraft:ore_metal", 0)
lead_ore = Ore("railcraft:ore_metal", 2)
nickel_ore = Ore("railcraft:ore_metal", 4)
silver_ore = Ore("railcraft:ore_metal", 3)
tin_ore = Ore("railcraft:ore_metal", 1)
zinc_ore = Ore("railcraft:ore_metal", 5)

# Minerals
diamond_dark_ore = Ore("railcraft:ore", 2)
emerald_dark_ore = Ore("railcraft:ore", 3)
firestone_ore = Ore("railcraft:ore_magic", 0)
lapis_dark_ore = Ore("railcraft:ore", 4)
saltpeter_ore = Ore("railcraft:ore", 1)
saltpeter_spawner = Ore("railcraft:worldlogic")
sulfur_ore = Ore("railcraft:ore", 0)

# Poor Metals
copper_poor_ore = Ore("railcraft:ore_metal_poor", 2)
gold_poor_ore = Ore("railcraft:ore_metal_poor", 1)
iron_poor_ore = Ore("railcraft:ore_metal_poor", 0)
lead_poor_ore = Ore("railcraft:ore_metal_poor", 4)
nickel_poor_ore = Ore("railcraft:ore_metal_poor", 6)
silver_poor_ore = Ore("railcraft:ore_metal_poor", 5)
tin_poor_ore = Ore("railcraft:ore_metal_poor", 3)
zinc_poor_ore = Ore("railcraft:ore_metal_poor", 7)

# Stone Variants
abyssal_stone = Ore("railcraft:generic", 8)
quaried_stone = Ore("railcraft:generic", 9)


# Veins ################################################################################################################

dark_diamond_vein = Vein(diamond_dark_ore, material_ore=abyssal_stone)
dark_emerald_vein = Vein(emerald_dark_ore, material_ore=abyssal_stone)
dark_lapis_vein = Vein(lapis_dark_ore, material_ore=abyssal_stone)
