"""Define various ores from the ModularForceFieldSystem mod."""

from pinerylabs.oregen import Ore, Vein
from pinerylabs.oregen.data import vanilla as mc


# Fluids ###############################################################################################################

aerotheum_fluid = Ore("thermalfoundation:fluid_aerotheum")
crude_oil_fluid = Ore("thermalfoundation:fluid_crude_oil")
cryotheum_fluid = Ore("thermalfoundation:fluid_cryotheum")
ender_fluid = Ore("thermalfoundation:fluid_ender")
glowstone_fluid = Ore("thermalfoundation:fluid_glowstone")
mana_fluid = Ore("thermalfoundation:fluid_mana")
petrotheum_fluid = Ore("thermalfoundation:fluid_petrotheum")
pyrotheum_fluid = Ore("thermalfoundation:fluid_pyrotheum")
redstone_fluid = Ore("thermalfoundation:fluid_redstone")


# Ores #################################################################################################################

# Clathrates
destabilized_redstone = Ore("thermalfoundation:ore_fluid", 2)
energized_netherrack = Ore("thermalfoundation:ore_fluid", 3)
gravel_oil_ore = Ore("thermalfoundation:ore_fluid", 1)
sand_oil_ore = Ore("thermalfoundation:ore_fluid", 0)
red_sand_oil_ore = Ore("thermalfoundation:ore_fluid", 5)
resonant_end_stone = Ore("thermalfoundation:ore_fluid", 4)

# Metals
aluminum_ore = Ore("thermalfoundation:ore", 4)
copper_ore = Ore("thermalfoundation:ore", 0)
iridium_ore = Ore("thermalfoundation:ore", 7)
lead_ore = Ore("thermalfoundation:ore", 3)
mithril_ore = Ore("thermalfoundation:ore", 8)
nickel_ore = Ore("thermalfoundation:ore", 5)
platinum_ore = Ore("thermalfoundation:ore", 6)
silver_ore = Ore("thermalfoundation:ore", 2)
tin_ore = Ore("thermalfoundation:ore", 1)


# Veins ################################################################################################################

# Clathrates
destablized_redstone_vein = Vein(destabilized_redstone)
energized_netherrack_vein = Vein(energized_netherrack, material_ore=mc.netherrack)
gravel_oil_vein = Vein(gravel_oil_ore, material_ore=mc.gravel)
sand_oil_vein = Vein(sand_oil_ore, material_ore=mc.sand)
red_sand_oil_vein = Vein(red_sand_oil_ore, material_ore=mc.red_sand)

# Metals
aluminum_vein = Vein(aluminum_ore)
copper_vein = Vein(copper_ore)
iridium_vein = Vein(iridium_ore)
lead_vein = Vein(lead_ore)
mithril_vein = Vein(mithril_ore)
nickel_vein = Vein(nickel_ore)
platinum_vein = Vein(platinum_ore)
silver_vein = Vein(silver_ore)
tin_vein = Vein(tin_ore)
