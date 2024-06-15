from dataclasses import dataclass

from generated.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointAbstract(PointVersionStructure):
    """A POINT where a control process is activated when a vehicle passes it.

    EQUIPMENT may be needed for the activation.
    """

    class Meta:
        name = "ActivationPoint_"
        namespace = "http://www.netex.org.uk/netex"
