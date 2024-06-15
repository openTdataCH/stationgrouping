from dataclasses import dataclass

from generated.compound_train_version_structure import (
    CompoundTrainVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrain(CompoundTrainVersionStructure):
    """
    A vehicle composed of COMPOUND TRAIN ELEMENTs in a certain order, i.e. of
    wagons assembled together and propelled by a locomotive or one of the wagons.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
