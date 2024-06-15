from dataclasses import dataclass

from generated.direction_value_structure import DirectionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Direction(DirectionValueStructure):
    """
    A classification for the general orientation of ROUTEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
