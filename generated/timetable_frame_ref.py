from dataclasses import dataclass

from generated.timetable_frame_ref_structure import TimetableFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetableFrameRef(TimetableFrameRefStructure):
    """
    Reference to a TIMETABLE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
