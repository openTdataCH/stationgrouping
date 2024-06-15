from dataclasses import dataclass

from generated.type_of_version_value_structure import (
    TypeOfVersionValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfVersion(TypeOfVersionValueStructure):
    """
    A classification of the VERSIONs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
