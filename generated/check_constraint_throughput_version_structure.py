from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.check_constraint_ref import CheckConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintThroughputVersionStructure(AssignmentVersionStructure1):
    """
    Type for a CHECK CONSTRAINT THROUGHPUT.

    :ivar check_constraint_ref:
    :ivar period: Interval for measurement.
    :ivar maximum_passengers: Maximum number of passengers.
    :ivar average_passengers: Average number of passengers.
    :ivar wheelchair_passengers: Maximum number of wheelchair
        passengers.
    """

    class Meta:
        name = "CheckConstraintThroughput_VersionStructure"

    check_constraint_ref: Optional[CheckConstraintRef] = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    average_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "AveragePassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
