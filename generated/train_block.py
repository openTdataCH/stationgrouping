from dataclasses import dataclass

from generated.train_block_version_structure import TrainBlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlock(TrainBlockVersionStructure):
    """A composite train formed of several BLOCKs coupled together during a certain
    period.

    Any coupling or separation action marks the start of a new TRAIN
    BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
