from dataclasses import dataclass

from generated.parking_charge_band_ref_structure import (
    ParkingChargeBandRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingChargeBandRef(ParkingChargeBandRefStructure):
    """
    Reference to a PARKING TARIFF CHARGE BAND.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
