from dataclasses import dataclass

from generated.distance_matrix_element_ref_by_value_structure import (
    DistanceMatrixElementRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementRefByValue(
    DistanceMatrixElementRefByValueStructure
):
    """
    Reference to a DISTANCE MATRIX ELEMENT LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
