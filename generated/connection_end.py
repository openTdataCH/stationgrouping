from dataclasses import dataclass

from generated.connection_end_structure import ConnectionEndStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionEnd(ConnectionEndStructure):
    """
    One end of a CONNECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
