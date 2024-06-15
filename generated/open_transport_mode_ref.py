from dataclasses import dataclass

from generated.open_transport_mode_ref_structure import (
    OpenTransportModeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTransportModeRef(OpenTransportModeRefStructure):
    """
    Reference to a TRANSPORT MODE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
