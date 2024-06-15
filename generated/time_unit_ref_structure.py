from dataclasses import dataclass

from generated.fare_unit_ref_structure import FareUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitRefStructure(FareUnitRefStructure):
    """
    Type for Reference to a TIME UNIT.
    """
