from dataclasses import dataclass

from generated.stop_area_version_structure import StopAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopArea(StopAreaVersionStructure):
    """
    A group of STOP POINTs close to each other.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
