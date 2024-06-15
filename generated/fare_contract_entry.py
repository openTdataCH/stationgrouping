from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractEntry(DataManagedObjectStructure):
    """
    Dummy type for FARE CONTRACT ENTRY.
    """

    class Meta:
        name = "FareContractEntry_"
        namespace = "http://www.netex.org.uk/netex"
