from dataclasses import dataclass

from generated.compound_block_structure import CompoundBlockStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundBlock(CompoundBlockStructure):
    """A composite BLOCK formed of several BLOCKs coupled together during a certain
    period.

    Any coupling or separation action marks the start of a new COMPOUND
    BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
