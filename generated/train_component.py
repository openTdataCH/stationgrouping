from dataclasses import dataclass

from generated.train_component_version_structure import (
    TrainComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponent(TrainComponentVersionStructure):
    """
    A specification of the order of TRAIN ELEMENTs in a TRAIN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
