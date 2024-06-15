from dataclasses import dataclass

from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZoneRefStructure(ZoneRefStructure):
    """Type for Reference to an ADMINISTRATIVE ZONE.

    Left untyped so as to avoid forwards dependency.
    """
