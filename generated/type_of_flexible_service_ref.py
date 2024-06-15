from dataclasses import dataclass

from generated.type_of_flexible_service_ref_structure import (
    TypeOfFlexibleServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFlexibleServiceRef(TypeOfFlexibleServiceRefStructure):
    """
    Reference to a TYPE OF FLEXIBLE SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
