from dataclasses import dataclass

from generated.parking_tariff_ref_structure import ParkingTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariffRef(ParkingTariffRefStructure):
    """
    Reference to a PARKING TARIFF.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
