from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRequirementVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE REQUIREMENT.

    :ivar name: Name of FACILITY REQUIREMENT.
    """

    class Meta:
        name = "VehicleRequirement_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
