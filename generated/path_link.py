from dataclasses import dataclass

from generated.path_link_version_structure import PathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLink(PathLinkVersionStructure):
    """
    A link between any two PLACEs (That is STOP PLACEs, ACCESS SPACEs or QUAYs,
    BOARDING POSITIONs, POINTs OF INTEREST etc or PATH JUNCTIONs) that represents a
    step in a possible route for pedestrians, cyclists or other out of vehicle
    passengers within or between a PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
