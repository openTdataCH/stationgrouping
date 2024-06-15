from dataclasses import dataclass

from generated.group_of_links_version_structure import (
    GroupOfLinksVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinks(GroupOfLinksVersionStructure):
    """
    A grouping of LINKs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
