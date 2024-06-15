from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityConditionAbstract(DataManagedObjectStructure):
    """Condition used in order to characterise a given VERSION of a VERSION FRAME.

    A VALIDITY CONDITION consists of a parameter (e.g. date, triggering
    event, etc) and its type of application (e.g. for, from, until,
    etc.).
    """

    class Meta:
        name = "ValidityCondition_"
        namespace = "http://www.netex.org.uk/netex"
