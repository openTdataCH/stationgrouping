from dataclasses import dataclass

from generated.block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockPart(BlockPartVersionStructure):
    """
    A part of a BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
