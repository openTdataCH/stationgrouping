from dataclasses import dataclass

from generated.site_component_version_structure import (
    SiteComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteComponent(SiteComponentVersionStructure):
    """An element of a SITE describing part of its structure.

    SITE COMPONENTs share common properties for accessibility and other
    features.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
