from dataclasses import dataclass

from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneRefStructure(ZoneRefStructure):
    """
    Type for a reference to a TARIFF ZONE.
    """
