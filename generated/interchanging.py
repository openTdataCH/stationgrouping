from dataclasses import dataclass

from generated.interchanging_version_structure import (
    InterchangingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Interchanging(InterchangingVersionStructure):
    """
    Limitations on making changes within a trip.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
