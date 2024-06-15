from dataclasses import dataclass

from generated.administrative_zone_ref_structure import (
    AdministrativeZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportAdministrativeZoneRefStructure(AdministrativeZoneRefStructure):
    """
    Type for a reference to a TRANSPORT ADMINISTRATIVE ZONE.
    """
