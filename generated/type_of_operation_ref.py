from dataclasses import dataclass

from generated.type_of_operation_ref_structure import (
    TypeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfOperationRef(TypeOfOperationRefStructure):
    """
    Reference to a TYPE OF OPERATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
