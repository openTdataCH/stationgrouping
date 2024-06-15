from dataclasses import dataclass

from generated.train_in_compound_train_ref_structure import (
    TrainInCompoundTrainRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    """
    Reference to a TRAIN IN COMPOUND TRAIN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
