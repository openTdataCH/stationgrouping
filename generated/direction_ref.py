from dataclasses import dataclass

from generated.direction_ref_structure import DirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionRef(DirectionRefStructure):
    """
    Reference to a DIRECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
