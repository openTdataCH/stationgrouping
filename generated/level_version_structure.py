from dataclasses import dataclass, field
from typing import Optional, Union

from generated.accessibility_assessment_versioned_child_structure import (
    AccessibilityAssessmentVersionedChildStructure,
)
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString
from generated.parking_ref import ParkingRef
from generated.point_of_interest_ref import PointOfInterestRef
from generated.service_site_ref import ServiceSiteRef
from generated.site_ref import SiteRef
from generated.stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelVersionStructure(DataManagedObjectStructure):
    """
    Type for a SITE LEVEL.

    :ivar name: Name of LEVEL.
    :ivar short_name: Short Name of LEVEL.
    :ivar description: Description of LEVEL.
    :ivar public_code: Public code for LEVEL.
    :ivar public_use: Whether level is for public use.
    :ivar accessibility_assessment: Accessibility values associated with
        LEVEL.
    :ivar all_areas_wheelchair_accessible: Whether all areas of the
        LEVEL are wheelchair accessible.
    :ivar choice:
    """

    class Meta:
        name = "Level_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: Optional[
        AccessibilityAssessmentVersionedChildStructure
    ] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
