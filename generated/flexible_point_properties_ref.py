from dataclasses import dataclass

from generated.flexible_point_properties_ref_structure import (
    FlexiblePointPropertiesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexiblePointPropertiesRef(FlexiblePointPropertiesRefStructure):
    """
    Reference to a FLEXIBLE POINT PROPERTies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
