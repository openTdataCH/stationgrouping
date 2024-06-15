from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartitionValueStructure(TypeOfValueVersionStructure):
    """
    Type for a PURPOSE OF JOURNEY PARTITION.
    """

    class Meta:
        name = "PurposeOfJourneyPartition_ValueStructure"
