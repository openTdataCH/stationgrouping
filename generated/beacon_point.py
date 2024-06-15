from dataclasses import dataclass

from generated.beacon_point_version_structure import (
    BeaconPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPoint(BeaconPointVersionStructure):
    """
    A POINT where a beacon or similar device to support the automatic detection of
    vehicles passing by is located.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
