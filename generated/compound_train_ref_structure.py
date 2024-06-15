from dataclasses import dataclass

from generated.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrainRefStructure(VehicleTypeRefStructure):
    """
    Type for a reference to a COMPOUND TRAIN.
    """