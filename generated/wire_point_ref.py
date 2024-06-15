from dataclasses import dataclass

from generated.wire_point_ref_structure import WirePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WirePointRef(WirePointRefStructure):
    """
    Reference to a WIRE POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
