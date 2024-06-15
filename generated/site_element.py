from dataclasses import dataclass

from generated.site_element_version_structure import (
    SiteElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteElement(SiteElementVersionStructure):
    """A physical PLACE to which passengers may go.

    May have ACCESSIBILITY ASSESMENT and other properties to describe
    it.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
