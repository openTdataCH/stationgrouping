from dataclasses import dataclass

from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZoneAbstract(ZoneVersionStructure):
    """
    Dummy supertype for ADMINISTRATIVE ZONE.
    """

    class Meta:
        name = "AdministrativeZone_"
        namespace = "http://www.netex.org.uk/netex"
