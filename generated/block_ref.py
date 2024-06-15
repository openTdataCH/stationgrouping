from dataclasses import dataclass

from generated.block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockRef(BlockRefStructure):
    """
    Reference to a BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
