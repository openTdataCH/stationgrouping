from dataclasses import dataclass

from generated.site_component_version_structure import (
    SiteComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestComponentVersionStructure(SiteComponentVersionStructure):
    """
    Type for a POINT OF INTEREST COMPONENT.
    """

    class Meta:
        name = "PointOfInterestComponent_VersionStructure"
