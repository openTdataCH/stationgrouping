from dataclasses import dataclass

from generated.info_link_structure import InfoLinkStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfoLink(InfoLinkStructure):
    """
    A hyperlink to an external web resource.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
