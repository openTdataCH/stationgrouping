from dataclasses import dataclass

from generated.train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainNumberRef(TrainNumberRefStructure):
    """
    Reference to a TRAIN NUMBER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
