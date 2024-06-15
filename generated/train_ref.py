from dataclasses import dataclass

from generated.train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainRef(TrainRefStructure):
    """
    Reference to a TRAIN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
