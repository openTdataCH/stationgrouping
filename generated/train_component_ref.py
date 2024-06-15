from dataclasses import dataclass

from generated.train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentRef(TrainComponentRefStructure):
    """
    Reference to a TRAIN COMPONENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
