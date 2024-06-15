from dataclasses import dataclass

from generated.purpose_of_journey_partition_ref_structure import (
    PurposeOfJourneyPartitionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartitionRef(PurposeOfJourneyPartitionRefStructure):
    """
    Reference to a PURPOSE OF JOURNEY PARTITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
