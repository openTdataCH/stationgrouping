from dataclasses import dataclass

from generated.beacon_point_ref_structure import BeaconPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPointRef(BeaconPointRefStructure):
    """
    Reference to a BEACON POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
