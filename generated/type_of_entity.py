from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEntity(TypeOfEntityVersionStructure):
    """
    A Type of value used to classify an ENTITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
