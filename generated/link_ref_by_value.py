from dataclasses import dataclass

from generated.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkRefByValue(LinkRefByValueStructure):
    """
    Reference to a LINK using its end values.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
