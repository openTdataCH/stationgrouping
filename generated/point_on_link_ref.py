from dataclasses import dataclass

from generated.point_on_link_ref_structure_1 import PointOnLinkRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLinkRef(PointOnLinkRefStructure1):
    """
    Reference to a POINT ON LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
