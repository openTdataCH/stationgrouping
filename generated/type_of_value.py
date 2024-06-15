from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfValue(TypeOfValueVersionStructure):
    """
    A code value from an extensible set, i.e.   which may be added to by user
    applications and is used to validate the properties of Entities.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
