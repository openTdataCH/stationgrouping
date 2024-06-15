from dataclasses import dataclass

from generated.course_of_journeys_version_structure import (
    CourseOfJourneysVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CourseOfJourneys(CourseOfJourneysVersionStructure):
    """
    A part of a BLOCK composed of consecutive VEHICLE JOURNEYs defined for the same
    DAY TYPE, all operated on the same LINE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
