from dataclasses import dataclass

from generated.transport_submode_structure import TransportSubmodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportSubmode(TransportSubmodeStructure):
    """
    A submode of a Public Transport MODE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
