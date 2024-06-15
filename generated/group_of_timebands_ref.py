from dataclasses import dataclass

from generated.group_of_timebands_ref_structure import (
    GroupOfTimebandsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebandsRef(GroupOfTimebandsRefStructure):
    """
    Reference to a GROUP OF TIMEBANDs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
