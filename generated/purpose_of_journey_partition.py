from dataclasses import dataclass

from generated.purpose_of_journey_partition_value_structure import (
    PurposeOfJourneyPartitionValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartition(PurposeOfJourneyPartitionValueStructure):
    """
    An operational purpose changing within a JOURNEY PATTERN and with this
    subdividing the SERVICE JOURNEY into JOURNEY PARTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
