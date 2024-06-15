from dataclasses import dataclass

from generated.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrafficControlPointVersionStructure(PointVersionStructure):
    """
    Type for TRAFFIC CONTROL POINT.
    """

    class Meta:
        name = "TrafficControlPoint_VersionStructure"
