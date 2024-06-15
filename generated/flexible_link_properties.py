from dataclasses import dataclass

from generated.flexible_link_properties_versioned_child_structure import (
    FlexibleLinkPropertiesVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLinkProperties(FlexibleLinkPropertiesVersionedChildStructure):
    """
    Flexible properties of a LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
