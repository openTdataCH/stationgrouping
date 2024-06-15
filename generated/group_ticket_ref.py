from dataclasses import dataclass

from generated.group_ticket_ref_structure import GroupTicketRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupTicketRef(GroupTicketRefStructure):
    """
    Reference to a GROUP TICKET usage parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
