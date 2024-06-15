from dataclasses import dataclass

from generated.vehicle_type_preference_ref_structure import (
    VehicleTypePreferenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypePreferenceRef(VehicleTypePreferenceRefStructure):
    """
    Reference to a VEHICLE TYPE PREFERENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
