"""Define the AsteroidFile class."""
from __future__ import annotations

import os

from io import FileIO
from typing import List
from xml.dom.minidom import Document, Node, getDOMImplementation

from packconfig.oregen import Asteroid


########################################################################################################################

class AsteroidFile(object):
    """AsteroidFile creates the content for an Advanced Rocketry asteroidConfig.xml file."""

    def __init__(self):
        """Create a new asteroid file."""
        self.asteroids: List[Asteroid] = []

    # Public Methods ###############################################################################

    def add_asteroid(self, asteroid: Asteroid):
        """Add an asteroid to this file."""
        self.asteroids.append(asteroid)

    def as_xml(self, document: Document) -> Node:
        """Create an XML node representing the asteriod list for this config file."""
        node = document.createElement("Asteroids")
        for asteroid in self.asteroids:
            node.appendChild(asteroid.as_xml(document))

        return node

    def print(self):
        """Print the content of this config file to the console."""
        document = getDOMImplementation().createDocument(None, None, None)
        node = self.as_xml(document)
        document.appendChild(node)
        print(document.toprettyxml(indent="    ", encoding="utf8"))

    def write_file(self, target_dir: str):
        """
        Write the content of this file to the given target directory.

        It will be assumed that that the target directory is the `config` directory for a modded Minecraft profile. The
        actual config file will be written into the `advRocketry/asteroidConfig.xml` file inside that directory.
        """
        document = getDOMImplementation().createDocument(None, None, None)
        node = self.as_xml(document)
        document.appendChild(node)
        text = document.toprettyxml(indent="    ", encoding="utf8")

        target_dir = os.path.join(target_dir, "advRocketry")
        os.makedirs(target_dir, exist_ok=True)
        with FileIO(os.path.join(target_dir, "asteroidConfig.xml"), "w") as f:
            f.write(text)

    # Magic Methods ################################################################################

    def __enter__(self) -> AsteroidFile:
        """Begin a context with this file."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Exit the context using this file."""
        return False
