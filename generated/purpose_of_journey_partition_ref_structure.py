from dataclasses import dataclass

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartitionRefStructure(TypeOfValueRefStructure):
    """
    Type for a PURPOSE OF JOURNEY PARTITION.
    """