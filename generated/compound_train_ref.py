from dataclasses import dataclass

from generated.compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrainRef(CompoundTrainRefStructure):
    """
    Reference to a COMPOUND TRAIN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
