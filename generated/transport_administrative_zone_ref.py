from dataclasses import dataclass

from generated.transport_administrative_zone_ref_structure import (
    TransportAdministrativeZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportAdministrativeZoneRef(TransportAdministrativeZoneRefStructure):
    """
    Reference to a TRANSPORT ADMINISTRATIVE ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
