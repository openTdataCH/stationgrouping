from dataclasses import dataclass

from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneRefAbstract(ZoneRefStructure):
    """
    Dummy type Reference to a TARIFF ZONE.
    """

    class Meta:
        name = "TariffZoneRef_"
        namespace = "http://www.netex.org.uk/netex"
