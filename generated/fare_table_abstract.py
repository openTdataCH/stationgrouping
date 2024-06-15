from dataclasses import dataclass

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableAbstract(GroupOfEntitiesVersionStructure):
    """
    A grouping of prices that may be associated with a DISTANCE MATRIX ELEMENT,
    FARE STRUCTURE ELEMENT or  other PRICEABLE OBJECT.
    """

    class Meta:
        name = "FareTable_"
        namespace = "http://www.netex.org.uk/netex"
