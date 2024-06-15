from dataclasses import dataclass

from generated.type_of_projection_ref_structure import (
    TypeOfProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProjectionRef(TypeOfProjectionRefStructure):
    """
    Reference to a TYPE OF PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
