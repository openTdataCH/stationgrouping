from dataclasses import dataclass

from generated.type_of_validity_ref_structure import TypeOfValidityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfValidityRef(TypeOfValidityRefStructure):
    """
    Reference to a TYPE OF VALIDITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
