from dataclasses import dataclass

from generated.check_constraint_delay_ref_structure import (
    CheckConstraintDelayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintDelayRef(CheckConstraintDelayRefStructure):
    """
    Identifier of a CHECK CONSTRAINT DELAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
