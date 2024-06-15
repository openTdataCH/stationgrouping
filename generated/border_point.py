from dataclasses import dataclass

from generated.border_point_value_structure import BorderPointValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPoint(BorderPointValueStructure):
    """
    Designated BORDER POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
