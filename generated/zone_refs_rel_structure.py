from dataclasses import dataclass, field
from typing import Optional, Union

from generated.access_zone_ref import AccessZoneRef
from generated.administrative_zone_ref import AdministrativeZoneRef
from generated.fare_zone_ref import FareZoneRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.stop_area_ref import StopAreaRef
from generated.tariff_zone_ref import TariffZoneRef
from generated.transport_administrative_zone_ref import (
    TransportAdministrativeZoneRef,
)
from generated.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of ZONEs.

    This is to workaround s bug in XMLSPY
    """

    class Meta:
        name = "zoneRefs_RelStructure"

    choice: Optional[
        Union[
            StopAreaRef,
            AccessZoneRef,
            TransportAdministrativeZoneRef,
            AdministrativeZoneRef,
            FareZoneRef,
            TariffZoneRef,
            ZoneRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
