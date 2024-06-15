from dataclasses import dataclass

from generated.connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionRef(ConnectionRefStructure):
    """
    Reference to a CONNECTION link.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
