from dataclasses import dataclass

from generated.check_constraint_throughput_version_structure import (
    CheckConstraintThroughputVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintThroughput(CheckConstraintThroughputVersionStructure):
    """Throughput of a CHECK CONSTRAINT.

    the number of passengers who can pass through it.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
