from dataclasses import dataclass, field
from typing import Optional

from generated.complex_feature_members_rel_structure import (
    ComplexFeatureMembersRelStructure,
)
from generated.group_of_points_version_structure import (
    GroupOfPointsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureVersionStructure(GroupOfPointsVersionStructure):
    """
    Type for a COMPLEX FEATURE.

    :ivar feature_members: Simple features making up COMPLEX FEATURE.
    """

    class Meta:
        name = "ComplexFeature_VersionStructure"

    feature_members: Optional[ComplexFeatureMembersRelStructure] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
