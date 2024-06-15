from dataclasses import dataclass

from generated.fare_contract_entry_version_structure import (
    FareContractEntryVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractEntryAbstract(FareContractEntryVersionStructure):
    """A log entry describing an event referring to the life of a FARE CONTRACT: initial contracting, sales, validation entries, etc. A subset of a FARE CONTRACT ENTRY is often materialised on a TRAVEL DOCUMENT."""

    class Meta:
        name = "FareContractEntry"
        namespace = "http://www.netex.org.uk/netex"
