from dataclasses import dataclass

from generated.flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideAreaRefStructure(FlexibleQuayRefStructure):
    """
    Type for Unique Reference to a HAIL AND RIDE AREA.
    """
