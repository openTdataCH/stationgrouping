from dataclasses import dataclass, field
from typing import Optional

from generated.infrastructure_link_restriction_version_structure import (
    InfrastructureLinkRestrictionVersionStructure,
)
from generated.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedManoeuvreVersionStructure(
    InfrastructureLinkRestrictionVersionStructure
):
    """
    Type for a MANOEUVRE.

    :ivar vehicle_type_ref: Identifier of TYPE OF VEHICLE making
        MANOEUVRE. If no Manouevre  applies to all vehicles.
    """

    class Meta:
        name = "RestrictedManoeuvre_VersionStructure"

    vehicle_type_ref: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
