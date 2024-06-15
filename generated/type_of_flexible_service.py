from dataclasses import dataclass

from generated.type_of_flexible_service_value_structure import (
    TypeOfFlexibleServiceValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFlexibleService(TypeOfFlexibleServiceValueStructure):
    """
    A classification of FLEXIBLE SERVICEs according to their functional purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
