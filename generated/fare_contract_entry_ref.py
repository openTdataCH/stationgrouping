from dataclasses import dataclass

from generated.fare_contract_entry_ref_structure import (
    FareContractEntryRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractEntryRef(FareContractEntryRefStructure):
    """
    Reference to a FARE CONTRACT ENTRY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
