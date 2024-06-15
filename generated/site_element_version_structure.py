from dataclasses import dataclass, field
from typing import List, Optional

from generated.access_mode_enumeration import AccessModeEnumeration
from generated.accessibility_assessment import AccessibilityAssessment
from generated.addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)
from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.covered_enumeration import CoveredEnumeration
from generated.gated_enumeration import GatedEnumeration
from generated.lighting_enumeration import LightingEnumeration
from generated.multilingual_string import MultilingualString
from generated.public_use_enumeration import PublicUseEnumeration
from generated.site_facility_sets_rel_structure import (
    SiteFacilitySetsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteElementVersionStructure(AddressablePlaceVersionStructure):
    """
    Type for a SITE ELEMENT.

    :ivar accessibility_assessment:
    :ivar access_modes: Allowed MODEs to access SITE ELEMENT.
    :ivar name_suffix: Further suffix to name that may be used in some
        contexts.
    :ivar alternative_names: Alternative names.
    :ivar cross_road: Name of a Road that crosses the Road the street
        near the SITE ELEMENT that can be used to describe its relative
        location.
    :ivar landmark: Name of a Landmark near the SITE ELEMENT that can be
        used to describe its relative location.
    :ivar public_use: Whether the component is available for public use
        or is restricted.
    :ivar covered: Whether the component is Indoors or outdoors. Default
        is Indoors.
    :ivar gated: Whether the component is within a gated area or freely
        accessible without a pass or ticket.
    :ivar lighting: Whether the component is lit or not. Default is well
        Lit.
    :ivar all_areas_wheelchair_accessible: Whether all areas of the
        component are wheelchair accessible.
    :ivar person_capacity: Total number of people that component can
        contain.
    :ivar facilities: Facilities available at SITe.
    """

    class Meta:
        name = "SiteElement_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_road: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    landmark: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Landmark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
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
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
