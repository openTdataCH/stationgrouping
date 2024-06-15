from dataclasses import dataclass

from generated.block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockPartRefStructure(BlockPartRefStructure):
    """
    Type for a reference to a TRAIN BLOCK PART.
    """
