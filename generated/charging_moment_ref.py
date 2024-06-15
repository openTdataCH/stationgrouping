from dataclasses import dataclass

from generated.charging_moment_ref_structure import ChargingMomentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMomentRef(ChargingMomentRefStructure):
    """Reference to a CHARGING MOMENT.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
