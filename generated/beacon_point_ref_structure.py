from dataclasses import dataclass

from generated.activation_point_ref_structure import (
    ActivationPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPointRefStructure(ActivationPointRefStructure):
    """
    Type for a reference to a BEACON POINT.
    """
