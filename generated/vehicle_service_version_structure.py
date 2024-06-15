from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString
from generated.vehicle_service_parts_rel_structure import (
    VehicleServicePartsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServiceVersionStructure(DataManagedObjectStructure):
    """
    Type for VEHICLE SERVICE.

    :ivar name: Name of VEHICLE SERVICE.
    :ivar description: Description of VEHICLE SERVICE.
    :ivar vehicle_service_parts: Parts of a VEHICLE SERVICE.
    """

    class Meta:
        name = "VehicleService_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    vehicle_service_parts: Optional[VehicleServicePartsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleServiceParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
