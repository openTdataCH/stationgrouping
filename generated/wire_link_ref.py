from dataclasses import dataclass

from generated.wire_link_ref_structure import WireLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireLinkRef(WireLinkRefStructure):
    """
    Reference to a WIRE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
