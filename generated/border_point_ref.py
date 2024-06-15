from dataclasses import dataclass

from generated.border_point_ref_structure import BorderPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointRef(BorderPointRefStructure):
    """Reference to a BORDER POINT.

    (TAP TSI B.1.3 Border Boint Code).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
