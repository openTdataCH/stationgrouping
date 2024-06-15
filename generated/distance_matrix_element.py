from dataclasses import dataclass

from generated.distance_matrix_element_version_structure import (
    DistanceMatrixElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElement(DistanceMatrixElementVersionStructure):
    """
    A cell of an origin-destination matrix for TARIFF ZONEs or STOP POINTs,
    expressing a fare distance for the corresponding trip: value in km, number of
    fare units etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
