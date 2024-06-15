from dataclasses import dataclass

from generated.flexible_line_derived_view_structure import (
    FlexibleLineDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineView(FlexibleLineDerivedViewStructure):
    """
    A group of FLEXIBLE ROUTEs of which is generally known to the public by a
    similar name or number and which have common booking arrangements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
