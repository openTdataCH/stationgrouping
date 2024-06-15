from dataclasses import dataclass

from generated.railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayPointRef(RailwayPointRefStructure):
    """
    Reference to a RAILWAY POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
