from dataclasses import dataclass

from generated.railway_link_ref_by_value_structure import (
    RailwayLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRefByValue(RailwayLinkRefByValueStructure):
    """
    Reference to a RAILWAY LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
