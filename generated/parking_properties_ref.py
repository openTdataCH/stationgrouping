from dataclasses import dataclass

from generated.parking_properties_ref_structure import (
    ParkingPropertiesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPropertiesRef(ParkingPropertiesRefStructure):
    """
    Reference to a PARKING PROPERTIES.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
