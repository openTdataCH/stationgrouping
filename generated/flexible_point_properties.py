from dataclasses import dataclass

from generated.flexible_point_properties_versioned_child_structure import (
    FlexiblePointPropertiesVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexiblePointProperties(FlexiblePointPropertiesVersionedChildStructure):
    """
    Flexible properties of a POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
