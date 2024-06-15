from dataclasses import dataclass

from generated.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneRef(TariffZoneRefStructure):
    """
    Reference to a TARIFF ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
