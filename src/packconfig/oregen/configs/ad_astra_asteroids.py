"""Define asteroid configuration for the Ad Astra modpack."""

from collections import namedtuple

from packconfig.oregen import Asteroid, AsteroidFile, Quantity, Vein
from packconfig.oregen.data import (
    advanced_rocketry as ar,
    extreme_reactors as er,
    railcraft as rc,
    thermal_foundation as tf,
    vanilla as mc,
)

__all__ = []


# Ores #################################################################################################################

# Metals
aluminum_ore = ar.aluminum_ore
copper_ore = rc.copper_ore
copper_poor_ore = rc.copper_poor_ore
gold_ore = mc.gold_ore
gold_poor_ore = rc.gold_poor_ore
iridium_ore = ar.iridium_ore
iron_ore = mc.iron_ore
iron_poor_ore = rc.iron_poor_ore
lead_ore = rc.lead_ore
lead_poor_ore = rc.lead_poor_ore
nickel_ore = rc.nickel_ore
nickel_poor_ore = rc.nickel_poor_ore
platinum_ore = tf.platinum_ore
silver_ore = rc.silver_ore
silver_poor_ore = rc.silver_poor_ore
tin_ore = rc.tin_ore
tin_poor_ore = rc.tin_poor_ore
titanium_ore = ar.titanium_ore
uranium_ore = er.yellorite_ore
zinc_ore = rc.zinc_ore
zinc_poor_ore = rc.zinc_poor_ore

# Stones
stone = mc.stone


# Config File ##########################################################################################################

base_asteroids = [
    Asteroid(
        name="Aluminum",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            aluminum_ore.weighted(60),
            zinc_ore.weighted(20),
            stone.weighted(10),
            zinc_poor_ore.weighted(5),
        ).with_purity(25)
    ),
    Asteroid(
        name="Bronze",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            copper_poor_ore.weighted(30),
            tin_poor_ore.weighted(30),
            copper_ore.weighted(20),
            tin_ore.weighted(20),
        ).with_purity(25)
    ),
    Asteroid(
        name="Copper",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            copper_ore.weighted(75),
            copper_poor_ore.weighted(15),
            gold_poor_ore.weighted(9),
            gold_ore.weighted(1),
        ).with_purity(25)
    ),
    Asteroid(
        name="Iron",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            iron_ore.weighted(65),
            iron_poor_ore.weighted(10),
            nickel_ore.weighted(15),
            nickel_poor_ore.weighted(10),
        ).with_purity(25)
    ),
    Asteroid(
        name="Lead",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            lead_ore.weighted(50),
            uranium_ore.weighted(25),
            silver_poor_ore.weighted(15),
            silver_ore.weighted(10),
        ).with_purity(25)
    ),
    Asteroid(
        name="Nickel",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
           nickel_ore.weighted(75),
           iron_ore.weighted(20),
           platinum_ore.weighted(4),
           iridium_ore.weighted(1)
        ).with_purity(25)
    ),
    Asteroid(
        name="Silver",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            stone.weighted(34),
            silver_poor_ore.weighted(23),
            silver_ore.weighted(10),
            gold_poor_ore.weighted(23),
            gold_ore.weighted(10),
        ).with_purity(25)
    ),
    Asteroid(
        name="Tin",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            tin_ore.weighted(55),
            zinc_ore.weighted(20),
            tin_poor_ore.weighted(15),
            zinc_poor_ore.weighted(5),
        ).with_purity(25)
    ),
    Asteroid(
        name="Titanium",
        distance=25,
        mass=64,
        weight=100,
        vein=Vein(
            titanium_ore.weighted(100),
        ).with_purity(25)
    ),
]

Band = namedtuple("AsteroidBand", "prefix distance mass purity weight")
asteroid_bands = [
    Band("Tiny", 35, 64, 0.10, 100),
    Band("Small", 75, 128, 0.15, 80),
    Band("Medium", 115, 256, 0.20, 60),
    Band("Large", 155, 512, 0.25, 40),
    Band("Huge", 195, 1024, 0.30, 20),
]

config = AsteroidFile()
for base in base_asteroids:
    for band in asteroid_bands:
        asteroid = base.clone()
        asteroid.name = f"{band.prefix} {asteroid.name}"
        asteroid.distance = band.distance
        asteroid.mass = Quantity(band.mass)
        asteroid.vein = asteroid.vein.with_purity(band.purity)
        asteroid.weight = band.weight
        config.add_asteroid(asteroid)
