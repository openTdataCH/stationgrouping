from dataclasses import dataclass, field
from typing import Optional

from generated.derived_view_structure import DerivedViewStructure
from generated.multilingual_string import MultilingualString
from generated.point_of_interest_classification_ref import (
    PointOfInterestClassificationRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestClassificationDerivedViewStructure(DerivedViewStructure):
    """
    Type for POINT OF INTEREST CLASSIFICATION VIEW.

    :ivar point_of_interest_classification_ref:
    :ivar name: Name of POINT OF INTEREST CLASSIFICATION.
    """

    class Meta:
        name = "PointOfInterestClassification_DerivedViewStructure"

    point_of_interest_classification_ref: Optional[
        PointOfInterestClassificationRef
    ] = field(
        default=None,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
