from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightParameterAssignmentAbstract(DataManagedObjectStructure):
    """
    The assignment of a fare parameter (referring to geography, time, quality or
    usage) to an element of a fare system (access right, validated access, control
    mean, etc.).
    """

    class Meta:
        name = "AccessRightParameterAssignment_"
        namespace = "http://www.netex.org.uk/netex"
