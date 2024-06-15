from dataclasses import dataclass

from generated.train_size_structure import TrainSizeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainSize(TrainSizeStructure):
    """
    Requirements for TRAIN SIZe.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
