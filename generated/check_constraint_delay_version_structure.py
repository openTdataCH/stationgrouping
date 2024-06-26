from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.check_constraint_ref import CheckConstraintRef
from generated.class_of_use_ref import ClassOfUseRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintDelayVersionStructure(AssignmentVersionStructure1):
    """
    Type for a CHECK CONSTRAINT DELAY.

    :ivar check_constraint_ref: Reference to a CHECK CONSTRAINT. Can be
        omitted if given by context.
    :ivar class_of_use_ref:
    :ivar minimum_likely_delay: Minimum duration needed to pass through
        CHECK CONSTRAINT.
    :ivar average_delay: Average duration expected to pass through
        Check.
    :ivar maximum_likely_delay: Maximum duration expected to pass
        through CHECK CONSTRAINT.
    """

    class Meta:
        name = "CheckConstraintDelay_VersionStructure"

    check_constraint_ref: Optional[CheckConstraintRef] = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    average_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AverageDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
