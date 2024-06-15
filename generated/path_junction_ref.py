from dataclasses import dataclass

from generated.path_junction_ref_structure import PathJunctionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunctionRef(PathJunctionRefStructure):
    """
    Reference to a PATH JUNCTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
