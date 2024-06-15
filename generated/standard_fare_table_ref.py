from dataclasses import dataclass

from generated.standard_fare_table_ref_structure import (
    StandardFareTableRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRef(StandardFareTableRefStructure):
    """
    Reference to a STANDARD FARE TABLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
