from dataclasses import dataclass

from generated.network_version_structure import NetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Network(NetworkVersionStructure):
    """
    A named grouping of LINEs under which a Transport network is known.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
