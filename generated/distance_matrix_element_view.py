from dataclasses import dataclass

from generated.distance_matrix_element_derived_view_structure import (
    DistanceMatrixElementDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementView(DistanceMatrixElementDerivedViewStructure):
    """
    Simplified  view of CONNECTING JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
