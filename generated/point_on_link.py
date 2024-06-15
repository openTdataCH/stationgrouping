from dataclasses import dataclass

from generated.point_on_link_versioned_child_structure import (
    PointOnLinkVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLink(PointOnLinkVersionedChildStructure):
    """
    A POINT on a LINK which is not needed for LINK definition, but may be used for
    other purposes, e.g. for purposes of AVM or PI, or for driver information.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
