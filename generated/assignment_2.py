from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Assignment2(DataManagedObjectStructure):
    """Dummy Abtsract Assignment An Assigment assigns a property  to an assignment
    element.

    It has a name and n order.
    """

    class Meta:
        name = "Assignment_"
        namespace = "http://www.netex.org.uk/netex"
