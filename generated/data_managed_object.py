from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataManagedObject(DataManagedObjectStructure):
    """
    An ENTITY in VERSION that can be associated with a RESPONSIBILITY SET that
    describes who has responsibility for managing the data.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
