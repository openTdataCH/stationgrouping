from dataclasses import dataclass

from generated.onward_service_link_derived_view_structure import (
    OnwardServiceLinkDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardServiceLinkView(OnwardServiceLinkDerivedViewStructure):
    """
    Information about an onwards SERVICE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
