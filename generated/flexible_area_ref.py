from dataclasses import dataclass

from generated.flexible_area_ref_structure import FlexibleAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleAreaRef(FlexibleAreaRefStructure):
    """
    Reference to a FLEXIBLE AREA.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
