from dataclasses import dataclass

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceGroupAbstract(GroupOfEntitiesVersionStructure):
    """
    A grouping of prices, allowing the grouping of numerous possible consumption
    elements into a limited number of price references, or to apply grouped
    increase, in value or percentage.
    """

    class Meta:
        name = "PriceGroup_"
        namespace = "http://www.netex.org.uk/netex"
