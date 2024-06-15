from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecification2(DataManagedObjectStructure):
    """
    Dummy type for FARE CONTRACT ENTRY.
    """

    class Meta:
        name = "TravelSpecification_"
        namespace = "http://www.netex.org.uk/netex"
