from dataclasses import dataclass

from generated.train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElementRef(TrainElementRefStructure):
    """
    Reference to a TRAIN ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
