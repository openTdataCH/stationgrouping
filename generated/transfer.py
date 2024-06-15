from dataclasses import dataclass

from generated.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Transfer(TransferVersionStructure):
    """The possibility of a passenger to transfer between two PLACEs.

    May have times associated for the transfer.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
