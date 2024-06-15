from dataclasses import dataclass

from generated.check_constraint_throughput_ref_structure import (
    CheckConstraintThroughputRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintThroughputRef(CheckConstraintThroughputRefStructure):
    """
    Identifier of a CHECK CONSTRAINT THROUGHPUT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
