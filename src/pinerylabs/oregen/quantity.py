"""Define the Quantity class."""
from __future__ import annotations

import random

from typing import Union


########################################################################################################################

class Quantity(object):
    """Quantity describes a value which may vary within a range."""

    def __init__(self, minimum: float, variance: float = 0):
        """Create a new quantity."""
        self.minimum = minimum
        self.variance = variance

    # Class Methods ################################################################################

    @staticmethod
    def convert(value: Union[Quantity, float]) -> Quantity:
        """Convert an unknown value into a quantity."""
        if value is None:
            return None

        if isinstance(value, Quantity):
            return value

        return Quantity(value * 1.0)

    # Properties ###################################################################################

    @property
    def random_value(self) -> float:
        """Generate a random value within the range allowed by this quantity."""
        return self.minimum + random.randfloat(0, self.variance)


########################################################################################################################

Quantityable = Union[None, Quantity, int, float]
