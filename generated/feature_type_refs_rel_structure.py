from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_feature_ref import TypeOfFeatureRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FeatureTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF FEATURE.

    :ivar type_of_feature_ref: Reference to a TYPE OF FEATURE.
    """

    class Meta:
        name = "featureTypeRefs_RelStructure"

    type_of_feature_ref: List[TypeOfFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
