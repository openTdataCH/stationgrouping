from dataclasses import dataclass

from generated.check_constraint_delay_version_structure import (
    CheckConstraintDelayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintDelay(CheckConstraintDelayVersionStructure):
    """
    Time penalty associated with a CHECK CONSTRAINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
