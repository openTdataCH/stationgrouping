from dataclasses import dataclass

from generated.activation_point_version_structure import (
    ActivationPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPointVersionStructure(ActivationPointVersionStructure):
    """
    Type for BEACON POINT.
    """

    class Meta:
        name = "BeaconPoint_VersionStructure"
