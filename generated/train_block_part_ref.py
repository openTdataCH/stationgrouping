from dataclasses import dataclass

from generated.train_block_part_ref_structure import TrainBlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockPartRef(TrainBlockPartRefStructure):
    """
    Reference to a TRAIN BLOCK PART.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
