from dataclasses import dataclass, field
from typing import List, Union

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.residential_qualification import ResidentialQualification
from generated.residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationsRelStructure(OneToManyRelationshipStructure):
    """
    Type for  a list of RESIDENTIAL QUALIFICATIONs.
    """

    class Meta:
        name = "residentialQualifications_RelStructure"

    residential_qualification_ref_or_residential_qualification: List[
        Union[ResidentialQualificationRef, ResidentialQualification]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationRef",
                    "type": ResidentialQualificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualification",
                    "type": ResidentialQualification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
