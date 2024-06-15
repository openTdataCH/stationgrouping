from dataclasses import dataclass

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfValueRef(TypeOfValueRefStructure):
    """Reference to a TYPE OF VALUE.

    Implementation of a one to one relationship by reference to  TYPE OF
    VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
