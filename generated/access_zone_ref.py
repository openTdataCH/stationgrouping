from dataclasses import dataclass

from generated.access_zone_ref_structure import AccessZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessZoneRef(AccessZoneRefStructure):
    """
    Reference to a SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
