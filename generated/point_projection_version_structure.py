from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.link_ref_structure import LinkRefStructure
from generated.point_ref_structure import PointRefStructure
from generated.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a POINT PROJECTION.

    :ivar projected_point_ref: Reference to point that is being
        projected. May be limited if given by Context.
    :ivar project_to_point_ref: Reference to point onto which projected
        point is being projected.
    :ivar project_to_link_ref: Link to on which point projects.
    :ivar distance: Distance along link to which point projects.
    """

    class Meta:
        name = "PointProjection_VersionStructure"

    projected_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    project_to_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    project_to_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
