from dataclasses import dataclass

from generated.destination_display_ref_structure import (
    DestinationDisplayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayRef(DestinationDisplayRefStructure):
    """
    Reference to a DESTINATION DISPLAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
