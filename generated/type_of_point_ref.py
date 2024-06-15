from dataclasses import dataclass

from generated.type_of_point_ref_structure import TypeOfPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPointRef(TypeOfPointRefStructure):
    """
    Reference to a TYPE OF POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
