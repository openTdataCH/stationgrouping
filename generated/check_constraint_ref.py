from dataclasses import dataclass

from generated.check_constraint_ref_structure import (
    CheckConstraintRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintRef(CheckConstraintRefStructure):
    """
    Identifier of a CHECK CONSTRAINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
