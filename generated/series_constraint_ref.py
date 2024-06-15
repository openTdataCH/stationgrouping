from dataclasses import dataclass

from generated.series_constraint_ref_structure_1 import (
    SeriesConstraintRefStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintRef(SeriesConstraintRefStructure1):
    """
    Reference to a SERIES CONSTRAINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
