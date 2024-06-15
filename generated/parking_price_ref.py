from dataclasses import dataclass

from generated.parking_price_ref_structure import ParkingPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPriceRef(ParkingPriceRefStructure):
    """
    Reference to a PARKING TARIFF PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
