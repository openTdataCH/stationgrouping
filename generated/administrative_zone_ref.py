from dataclasses import dataclass

from generated.administrative_zone_ref_structure import (
    AdministrativeZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZoneRef(AdministrativeZoneRefStructure):
    """
    Reference to an ADMINISTRATIVE ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
