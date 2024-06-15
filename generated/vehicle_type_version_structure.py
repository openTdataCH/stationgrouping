from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.facility_requirements_rel_structure import (
    FacilityRequirementsRelStructure,
)
from generated.multilingual_string import MultilingualString
from generated.passenger_capacities_rel_structure import (
    PassengerCapacitiesRelStructure,
)
from generated.passenger_capacity_structure import PassengerCapacityStructure
from generated.passenger_carrying_requirements_rel_structure import (
    PassengerCarryingRequirementsRelStructure,
)
from generated.private_code import PrivateCode
from generated.service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from generated.type_of_fuel_enumeration import TypeOfFuelEnumeration
from generated.vehicle_manoeuvring_requirements_rel_structure import (
    VehicleManoeuvringRequirementsRelStructure,
)
from generated.vehicle_model_ref_structure import VehicleModelRefStructure
from generated.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE TYPE.

    :ivar name: Name of VEHICLE TYPE.
    :ivar short_name: Short Name of VEHICLE TYPE.
    :ivar description: Description of VEHICLE TYPE.
    :ivar private_code:
    :ivar reversing_direction: Whether vehicles of the type have a
        reversing direction.
    :ivar self_propelled: Whether vehicles of the type are self-
        propelled.
    :ivar type_of_fuel: The type of fuel used by a vehicle of the type.
    :ivar euro_class: Euroclass of the vehicle type.
    :ivar passenger_capacity: Total Number of passengers that VEHICLE
        TYPE can carry.
    :ivar capacities: Break down of Capacities by FARE CLASS.
    :ivar low_floor: Whether Vehicle is low floor to facilitate access
        by the mobility impaired.
    :ivar has_lift_or_ramp: Whether vehicle has lift or ramp to
        facilitate wheelchair access.
    :ivar has_hoist: Whether vehicle has hoist for wheelchair access.
    :ivar boarding_height: Maximum step height to board. +v1.1
    :ivar gap_to_platform: Expected maximal gap between VEHICLE and
        platform. +v1.1
    :ivar length: The length of a VEHICLE of the type.
    :ivar width: The width of a VEHICLE of the type. +v1.1
    :ivar height: The height of a VEHICLE of the type. +v1.1
    :ivar weight: The weight of a VEHICLE of the type. +v1.1
    :ivar included_in: Included in definition of VEHICLE.
    :ivar classified_as_ref: Classification of type as being of a
        particular VEHICLE MODEL.
    :ivar facilities: Facilities of VEHICLE TYPE.
    :ivar can_carry: Capacity that VEHICLE TYPE should meet - indicates
        minimum number of seats of each type.
    :ivar can_manoeuvre: Manoeuvring capabilities that VEHICLE TYPE
        should meet.
    :ivar satisfies_facility_requirements: FACILITIES requirements that
        VEHICLE TYPE should meet.
    """

    class Meta:
        name = "VehicleType_VersionStructure"

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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fuel: Optional[TypeOfFuelEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_capacity: Optional[PassengerCapacityStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    capacities: Optional[PassengerCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    included_in: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "IncludedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classified_as_ref: Optional[VehicleModelRefStructure] = field(
        default=None,
        metadata={
            "name": "ClassifiedAsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_carry: Optional[PassengerCarryingRequirementsRelStructure] = field(
        default=None,
        metadata={
            "name": "canCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_manoeuvre: Optional[VehicleManoeuvringRequirementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "canManoeuvre",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    satisfies_facility_requirements: Optional[
        FacilityRequirementsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "satisfiesFacilityRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
