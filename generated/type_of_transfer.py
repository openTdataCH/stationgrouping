from dataclasses import dataclass

from generated.type_of_transfer_value_structure import (
    TypeOfTransferValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTransfer(TypeOfTransferValueStructure):
    """
    Classification of a TRANSFER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
