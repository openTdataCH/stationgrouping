from dataclasses import dataclass

from generated.fare_zone_version_structure import FareZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZone(FareZoneVersionStructure):
    """
    A specialization of TARIFF ZONE to include FARE SECTIONs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
