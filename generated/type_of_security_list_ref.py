from dataclasses import dataclass

from generated.type_of_security_list_ref_structure import (
    TypeOfSecurityListRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfSecurityListRef(TypeOfSecurityListRefStructure):
    """
    Reference to a TYPE OF SECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
