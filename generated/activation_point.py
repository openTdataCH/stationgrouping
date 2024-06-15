from dataclasses import dataclass

from generated.activation_point_version_structure import (
    ActivationPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPoint(ActivationPointVersionStructure):
    """A POINT where a control process is activated when a vehicle passes it.

    EQUIPMENT may be needed for the activation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
