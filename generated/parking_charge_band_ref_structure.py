from dataclasses import dataclass

from generated.time_structure_factor_ref_structure import (
    TimeStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingChargeBandRefStructure(TimeStructureFactorRefStructure):
    """
    Type for a reference to a PARKING TARIFF CHARGE BAND.
    """
