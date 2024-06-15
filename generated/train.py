from dataclasses import dataclass

from generated.train_version_structure import TrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Train(TrainVersionStructure):
    """
    A vehicle composed of TRAIN ELEMENTs in a certain order, i.e. of wagons
    assembled together and propelled by a locomotive or one of the wagons.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
