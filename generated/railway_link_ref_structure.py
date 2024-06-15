from dataclasses import dataclass

from generated.infrastructure_link_ref_structure import (
    InfrastructureLinkRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRefStructure(InfrastructureLinkRefStructure):
    """
    Type for Reference to a RAILWAY LINK.
    """
