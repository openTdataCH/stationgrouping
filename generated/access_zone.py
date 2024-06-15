from dataclasses import dataclass

from generated.access_zone_version_structure import AccessZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessZone(AccessZoneVersionStructure):
    """An identified storey (ground, first, basement, mezzanine, etc) within an
    interchange building or SITE on which SITE COMPONENTs reside.

    A PATH LINK may connect components on different ACCESS ZONEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
