"""Define the Ore class."""
from __future__ import annotations

from typing import Any, Dict, Iterable, Union

from pinerylabs.oregen import Ore


########################################################################################################################

class OreList(object):
    """OreList defines a grouping of ores."""

    def __init__(self, *ores: Iterable[Ore]):
        """Create a new ore list."""
        self._ores = []
        self.add(*ores)

    # Class Methods ################################################################################

    @staticmethod
    def convert(arg: OreListable) -> OreList:
        """Convert an orelist-able object into an actual OreList."""
        if arg is None:
            return None
        elif isinstance(arg, str):
            return OreList(Ore(arg))
        elif isinstance(arg, Ore):
            return OreList(arg)
        elif isinstance(arg, OreList):
            return arg
        else:
            ores = []
            for ore in arg:
                if isinstance(ore, Ore):
                    ores.append(ore)
            return OreList(*ores)

    # Class Methods ################################################################################

    @staticmethod
    def merge(self, *ore_lists: OreList) -> OreList:
        """Merge the contents of several ore lists into a new one."""
        result = OreList()
        for ore_list in ore_lists:
            result.add(*ore_list.ores)

        return result

    # Properties ###################################################################################

    @property
    def is_empty(self) -> bool:
        """Determine whether there are any ores in this collection."""
        return len(self._ores) == 0

    @property
    def ores(self) -> Iterable[Ore]:
        """Iterate over the ores in this list."""
        for ore in self._ores:
            yield ore

    @property
    def short_name(self) -> str:
        """Get the short name of this ore (i.e., without the mod name)."""
        if len(self._ores) == 0:
            return "empty_ore_list"
        elif len(self._ores) == 1:
            return self._ores[0].short_name
        else:
            return f"{self._ores[0].short_name}_etc"

    # Methods ######################################################################################

    def add(self, *ores: Iterable[Ore]) -> OreList:
        """Add a new ore to this list."""
        for ore in ores:
            if not isinstance(ore, Ore):
                raise TypeError(f"cannot add a {type(ore).__name__} to an OreList")

            self._ores.append(ore)

        return self

    def as_json(self) -> Dict[str, Any]:
        """Create a dict representation of this ore suitable for being converted to JSON."""
        if len(self._ores) == 0:
            return []
        elif len(self._ores) == 1:
            return self._ores[0].as_json()
        else:
            return [o.as_json() for o in self._ores]

    def scaled(self, percent: float) -> Ore:
        """
        Create a copy of this list which each ore in it scaled by the given percent.

        Arguments:
            percent: a value between 0 and 100 indicating how much to scale the ores' weights

        Returns:
            a new list containing new ores which have been scaled as requested

        """
        return [o.weighted(o.weight * (percent / 100.0)) for o in self._ores]

    # Overridden Methods ###########################################################################

    def __repr__(self) -> str:
        """Get a string representation of this object."""
        result = ["OreList<"]
        needsDelimiter = False
        for ore in self._ores:
            if needsDelimiter:
                result.append(", ")
            result.append(str(ore))
            needsDelimiter = True

        result.append(">")
        return "".join(result)


########################################################################################################################

OreListable = Union[Iterable[Ore], None, Ore, OreList, str]
