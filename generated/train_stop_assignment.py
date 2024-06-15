from dataclasses import dataclass

from generated.train_stop_assignment_version_structure import (
    TrainStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainStopAssignment(TrainStopAssignmentVersionStructure):
    """Assignment of a scheduled train stop point to a STOP PLACE and quay.

    etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
