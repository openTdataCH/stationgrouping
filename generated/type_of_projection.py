from dataclasses import dataclass

from generated.type_of_projection_value_structure import (
    TypeOfProjectionValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProjection(TypeOfProjectionValueStructure):
    """
    Classification of a PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
