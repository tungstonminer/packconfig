"""Define the Crop Yield class."""

from typing import Optional

from packconfig import Range


########################################################################################################################

class CropYield(object):
    """CropYield represents a quantity of items produced by a certain plant when harvested."""

    def __init__(
        self,
        item_id: str,
        output_range: Optional[Range] = None,
        chance: Optional[float] = None,
    ):
        """Create a new crop yield."""
        super().__init__()

        if output_range is None:
            output_range = Range(1, 1)

        if chance is None:
            chance = 0.9

        self.item_id = item_id
        self.output_range = output_range
        self.chance = chance
