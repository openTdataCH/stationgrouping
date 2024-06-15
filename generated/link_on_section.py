from dataclasses import dataclass

from generated.link_on_section_versioned_child_structure import (
    LinkOnSectionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkOnSection(LinkOnSectionVersionedChildStructure):
    """LINK on a SECTION.

    +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
