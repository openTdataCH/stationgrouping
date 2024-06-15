from dataclasses import dataclass

from generated.flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleAreaRefStructure(FlexibleQuayRefStructure):
    """
    Type for reference to a FLEXIBLE AREA.
    """
