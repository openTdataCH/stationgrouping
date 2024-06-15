from dataclasses import dataclass

from generated.entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntranceRefStructure(EntranceRefStructure):
    """
    Type for reference to a POINT OF INTEREST VEHICLE ENTRANCE.
    """
