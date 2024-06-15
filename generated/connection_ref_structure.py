from dataclasses import dataclass

from generated.transfer_ref_structure import TransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionRefStructure(TransferRefStructure):
    """
    Type for a reference to a CONNECTION link.
    """
