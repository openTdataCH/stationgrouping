from dataclasses import dataclass

from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralZoneVersionStructure(ZoneVersionStructure):
    """
    Type for a General ZONE.
    """

    class Meta:
        name = "GeneralZone_VersionStructure"
