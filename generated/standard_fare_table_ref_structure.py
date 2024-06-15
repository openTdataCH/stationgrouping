from dataclasses import dataclass

from generated.fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRefStructure(FareTableRefStructure):
    """
    Type for Reference to a FARE STANDARD FARE TABLE.
    """
