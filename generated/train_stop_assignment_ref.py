from dataclasses import dataclass

from generated.train_stop_assignment_ref_structure import (
    TrainStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainStopAssignmentRef(TrainStopAssignmentRefStructure):
    """
    Reference to a TRAIN STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
