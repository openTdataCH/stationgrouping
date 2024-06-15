from dataclasses import dataclass

from generated.wire_element_version_structure import (
    WireElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireElement(WireElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a WIRE network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
