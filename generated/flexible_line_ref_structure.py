from dataclasses import dataclass

from generated.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineRefStructure(LineRefStructure):
    """
    Type for a reference to a FLEXIBLE LINE.
    """
