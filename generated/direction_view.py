from dataclasses import dataclass

from generated.direction_derived_view_structure import (
    DirectionDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionView(DirectionDerivedViewStructure):
    """
    Simplified View of DIRECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
