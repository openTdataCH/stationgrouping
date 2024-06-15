from dataclasses import dataclass

from generated.tariff_zone_version_structure import TariffZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZone(TariffZoneVersionStructure):
    """
    A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix
    system.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
