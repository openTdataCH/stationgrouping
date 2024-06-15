from dataclasses import dataclass

from generated.type_of_security_list_version_structure import (
    TypeOfSecurityListVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfSecurityList(TypeOfSecurityListVersionStructure):
    """A classification of SECURITY LIST.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
