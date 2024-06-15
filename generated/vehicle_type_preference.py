from dataclasses import dataclass

from generated.vehicle_type_preference_versioned_child_structure import (
    VehicleTypePreferenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypePreference(VehicleTypePreferenceVersionedChildStructure):
    """The preference for the use of a particular VEHICLE TYPE for a SERVICE
    JOURNEY PATTERN, depending on the DAY TYPE and TIME DEMAND TYPE.

    The rank of preferences must be recorded. Different VEHICLE TYPEs
    may be given the same rank.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
