from dataclasses import dataclass

from generated.fare_contract_entry_ref_structure import (
    FareContractEntryRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionRefStructure(FareContractEntryRefStructure):
    """
    Type for Reference to a SALES TRANSACTION.
    """
