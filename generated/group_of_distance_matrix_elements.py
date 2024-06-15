from dataclasses import dataclass

from generated.group_of_distance_matrix_elements_version_structure import (
    GroupOfDistanceMatrixElementsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfDistanceMatrixElements(
    GroupOfDistanceMatrixElementsVersionStructure
):
    """
    A group of DISTANCE MATRIX ELEMENTs; may set common properties for a given set
    of origin and destination pairs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
