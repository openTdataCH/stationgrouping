from dataclasses import dataclass

from generated.timetabled_passing_time_view_structure import (
    TimetabledPassingTimeViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetabledPassingTimeView(TimetabledPassingTimeViewStructure):
    """
    Simplified TIMETABLED PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
