from dataclasses import dataclass

from generated.block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockPartRef(BlockPartRefStructure):
    """
    Reference to a BLOCK PART.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
