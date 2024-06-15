from dataclasses import dataclass

from generated.standard_fare_table_version_structure import (
    StandardFareTableVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTable(StandardFareTableVersionStructure):
    """
    A set of price for a combination of price features in a Tariff.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
