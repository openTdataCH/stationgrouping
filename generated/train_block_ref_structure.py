from dataclasses import dataclass

from generated.block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockRefStructure(BlockRefStructure):
    """
    Type for a reference to a TRAIN BLOCK.
    """
