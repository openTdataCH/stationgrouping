from dataclasses import dataclass, field
from typing import Optional

from generated.train_components_rel_structure import (
    TrainComponentsRelStructure,
)
from generated.train_size import TrainSize
from generated.vehicle_type_version_structure import (
    VehicleTypeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainVersionStructure(VehicleTypeVersionStructure):
    """
    Type for TRAIN.

    :ivar train_size:
    :ivar components: Ordered collection of TRAIN COMPONENTs making up
        TRAIN.
    """

    class Meta:
        name = "Train_VersionStructure"

    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    components: Optional[TrainComponentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
