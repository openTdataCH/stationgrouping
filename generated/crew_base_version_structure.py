from dataclasses import dataclass, field
from typing import Optional, Union

from generated.garage_point_ref import GaragePointRef
from generated.garage_refs_rel_structure import GarageRefsRelStructure
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.parking_point_ref import ParkingPointRef
from generated.relief_point_ref import ReliefPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBaseVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for CREW BASE.

    :ivar garage_point_ref_or_parking_point_ref_or_relief_point_ref:
    :ivar garages: garages associated with CREW BASe.
    """

    class Meta:
        name = "CrewBase_VersionStructure"

    garage_point_ref_or_parking_point_ref_or_relief_point_ref: Optional[
        Union[GaragePointRef, ParkingPointRef, ReliefPointRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    garages: Optional[GarageRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
