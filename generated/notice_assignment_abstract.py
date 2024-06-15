from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentAbstract(DataManagedObjectStructure):
    """
    Dummy abstract NOTICE ASSIGNMENT.
    """

    class Meta:
        name = "NoticeAssignment_"
        namespace = "http://www.netex.org.uk/netex"
