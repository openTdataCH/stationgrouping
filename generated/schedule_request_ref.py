from dataclasses import dataclass

from generated.schedule_request_ref_structure import (
    ScheduleRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduleRequestRef(ScheduleRequestRefStructure):
    """
    Reference to a SCHEDULE REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
