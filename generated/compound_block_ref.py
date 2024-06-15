from dataclasses import dataclass

from generated.compound_block_ref_structure import CompoundBlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundBlockRef(CompoundBlockRefStructure):
    """
    Reference to a COMPOUND BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
