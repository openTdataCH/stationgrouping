from dataclasses import dataclass

from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessZoneRefStructure(ZoneRefStructure):
    """
    Type for reference to an ACCESS ZONE.
    """
