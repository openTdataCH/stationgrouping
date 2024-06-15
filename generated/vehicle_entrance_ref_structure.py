from dataclasses import dataclass

from generated.entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEntranceRefStructure(EntranceRefStructure):
    """
    Type for a reference to identifier of an VEHICLE ENTRANCE.
    """
