from dataclasses import dataclass

from generated.general_zone_version_structure import (
    GeneralZoneVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralZone(GeneralZoneVersionStructure):
    """
    A GENERAL ZONE used to define a zonal fare structure in a zone-counting or
    zone-matrix system.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
