from dataclasses import dataclass

from generated.group_of_link_sequences_version_structure import (
    GroupOfLinkSequencesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinkSequences(GroupOfLinkSequencesVersionStructure):
    """
    A grouping of LINK SEQUENCEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
