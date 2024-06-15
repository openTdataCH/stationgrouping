from dataclasses import dataclass

from generated.destination_display_version_structure import (
    DestinationDisplayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplay(DestinationDisplayVersionStructure):
    """
    An advertised destination of a specific JOURNEY PATTERN, usually displayed on a
    head sign or at other on-board locations.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
