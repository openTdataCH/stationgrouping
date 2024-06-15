from dataclasses import dataclass

from generated.type_of_transfer_ref_structure import TypeOfTransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTransferRef(TypeOfTransferRefStructure):
    """
    Reference to a TYPE OF TRANSFER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
