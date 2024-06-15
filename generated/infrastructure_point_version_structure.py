from dataclasses import dataclass

from generated.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructurePointVersionStructure(PointVersionStructure):
    """
    Type for INFRASTRUCTURE POINT.
    """

    class Meta:
        name = "InfrastructurePoint_VersionStructure"
