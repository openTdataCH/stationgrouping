from dataclasses import dataclass

from generated.transfer_duration_structure import TransferDurationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferDuration(TransferDurationStructure):
    """
    Times for TRANSFER between two Points.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
