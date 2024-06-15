from dataclasses import dataclass

from generated.type_of_link_ref_structure import TypeOfLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkRef(TypeOfLinkRefStructure):
    """
    Reference to a TYPE OF LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
