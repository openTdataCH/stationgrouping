from dataclasses import dataclass, field
from typing import List, Union

from generated.geographical_structure_factor import GeographicalStructureFactor
from generated.geographical_structure_factor_ref import (
    GeographicalStructureFactorRef,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactorsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of GEOGRAPHICAL STRUCTURE FACTOR.
    """

    class Meta:
        name = "geographicalStructureFactors_RelStructure"

    geographical_structure_factor_ref_or_geographical_structure_factor: List[
        Union[GeographicalStructureFactorRef, GeographicalStructureFactor]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
