from dataclasses import dataclass

from generated.railway_element_version_structure import (
    RailwayElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayElement(RailwayElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a RAILWAY network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
