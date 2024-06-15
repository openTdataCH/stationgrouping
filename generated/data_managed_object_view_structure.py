from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataManagedObjectViewStructure(DataManagedObjectStructure):
    """
    Type for MANAGED OBJECT VIEW.
    """

    class Meta:
        name = "DataManagedObject_ViewStructure"
