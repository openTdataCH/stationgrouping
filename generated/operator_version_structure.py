from dataclasses import dataclass, field
from typing import Any, ForwardRef, List, Optional, Union

from generated.contact_structure import ContactStructure
from generated.country_ref import CountryRef
from generated.departments_rel_structure import DepartmentsRelStructure
from generated.operator_activities_enumeration import (
    OperatorActivitiesEnumeration,
)
from generated.organisation_version_structure import (
    OrganisationVersionStructure,
)
from generated.postal_address import PostalAddress
from generated.postal_address_version_structure import (
    PostalAddressVersionStructure,
)
from generated.road_address import RoadAddress
from generated.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorVersionStructure(OrganisationVersionStructure):
    """
    Type for an OPERATOR.

    :ivar country_ref:
    :ivar postal_address_or_road_address_or_address:
    :ivar primary_mode: Primary transport MODE of OPERATOR
    :ivar operator_activities: Activities undertaken by OPERATOR.
    :ivar customer_service_contact_details: Contact details for Customer
        service use.
    :ivar departments: Departments of OPERATOR.
    """

    class Meta:
        name = "Operator_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address_or_road_address_or_address: Optional[
        Union[PostalAddress, RoadAddress, "OperatorVersionStructure.Address"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Address",
                    "type": ForwardRef("OperatorVersionStructure.Address"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    primary_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "PrimaryMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_activities: List[OperatorActivitiesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OperatorActivities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    customer_service_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departments: Optional[DepartmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class Address(PostalAddressVersionStructure):
        """
        :ivar types: Classification of ZONE. Used for arbitrary
            documentation -.
        :ivar centroid: Centre Coordinates of ZONE.
        :ivar polygon:
        :ivar projections: Projections of ZONE onto another layer.
        :ivar parent_zone_ref: Parent ZONE that contains this ZONE.
        :ivar members: POINTs in GROUP OF POINTs.
        :ivar key_list: A list of alternative Key values for an element.
        :ivar extensions:
        :ivar branding_ref:
        :ivar validity_conditions_or_valid_between:
        :ivar alternative_texts: Additional Translations of text
            elements.
        """

        types: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        centroid: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        polygon: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        projections: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        parent_zone_ref: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        members: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        key_list: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        extensions: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        branding_ref: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        validity_conditions_or_valid_between: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        alternative_texts: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
