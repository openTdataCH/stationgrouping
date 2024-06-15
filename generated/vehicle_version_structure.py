from dataclasses import dataclass, field
from typing import Optional, Union

from generated.compound_train_ref import CompoundTrainRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.equipments_rel_structure import EquipmentsRelStructure
from generated.multilingual_string import MultilingualString
from generated.operator_ref import OperatorRef
from generated.private_code import PrivateCode
from generated.train_ref import TrainRef
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE.

    :ivar name: Name of VEHICLE.
    :ivar short_name: Short Name of VEHICLE.
    :ivar registration_number: Licence plate of VEHICLE.
    :ivar operational_number: Operational Number of VEHICLE.
    :ivar private_code:
    :ivar operator_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar actual_vehicle_equipments: ACTUAL EQUIPMENT found in VEHICLE.
    """

    class Meta:
        name = "Vehicle_VersionStructure"

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
    registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalNumber",
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
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    actual_vehicle_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "actualVehicleEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
