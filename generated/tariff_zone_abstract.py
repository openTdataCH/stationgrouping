from dataclasses import dataclass

from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneAbstract(ZoneVersionStructure):
    """
    Dummy TARIFF ZONE  to workaround xML spy Substitution Group limitations.
    """

    class Meta:
        name = "TariffZone_"
        namespace = "http://www.netex.org.uk/netex"
