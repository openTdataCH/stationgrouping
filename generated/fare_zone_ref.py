from dataclasses import dataclass

from generated.fare_zone_ref_structure import FareZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRef(FareZoneRefStructure):
    """
    Reference to a FARE ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
