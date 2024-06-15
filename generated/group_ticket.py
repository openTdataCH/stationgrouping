from dataclasses import dataclass

from generated.group_ticket_version_structure import (
    GroupTicketVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupTicket(GroupTicketVersionStructure):
    """
    The number and characteristics of persons entitled to travel in addition to the
    holder of an access right.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
