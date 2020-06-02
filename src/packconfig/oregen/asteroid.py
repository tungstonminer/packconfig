"""Define the Asteriod class."""
from __future__ import annotations

from xml.dom.minidom import Document, Node

from packconfig.oregen import Ore, Quantity, Quantityable, Vein


########################################################################################################################

class Asteroid(object):
    """Asteriod defines configs for Advanced Rocketry asteriods' size, composition, and location."""

    def __init__(
        self,
        name: str,
        vein: Vein,
        distance: int = 10,
        mass: Quantityable = 100,
        weight: int = 1000,
    ):
        """
        Create a new asteriod.

        Arguments:
            name: a string giving the user-visible name of this type of asteriod
            veins: an iterable collection of Vein objects describing the ores available in this asteriod
            distnace: how many astronomical units away is this kind of asteroid. More valuable ones should generally
                be more distant
            mass: a range giving the total number of blocks in the asteriod
            weight: how probable is it that this asteriod will be detected compared to others
            purity: what percentage of this asteriod is ore vs stone (0 is all stone, 100 is all ore)

        """
        self.name = name
        self.distance = distance
        self.mass = Quantity.convert(mass)
        self.weight = weight
        self.vein = vein

    # Public Methods ###############################################################################

    def as_xml(self, document: Document) -> Node:
        """Create an XML node representing this asteroid."""
        node = document.createElement("asteroid")
        node.setAttribute("name", self.name)
        node.setAttribute("distance", str(self.distance))
        node.setAttribute("mass", str(self.mass.minimum))
        node.setAttribute("massVariability", str(self.mass.variance))
        node.setAttribute("minLevel", "0")
        node.setAttribute("probability", str(self.weight / 100.0))
        node.setAttribute("richness", str(self.vein.purity))
        node.setAttribute("richnessVariability", "0.25")

        ore: Ore = None
        for ore in self.vein.ores.ores:
            ore_node = document.createElement("ore")

            stack_name = ore.name
            if ore.metadata != 0:
                stack_name += f" {ore.metadata}"
            ore_node.setAttribute("itemStack", stack_name)

            ore_node.setAttribute("chance", str(ore.weight))

            node.appendChild(ore_node)

        return node

    def clone(self) -> Asteroid:
        """Return a clone of this asteroid config."""
        return Asteroid(self.name, self.vein.clone(), self.distance, self.mass, self.weight)
