from dataclasses import dataclass

from generated.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRefStructure(TariffZoneRefStructure):
    """
    Type for Reference to a FARE ZONE.
    """
