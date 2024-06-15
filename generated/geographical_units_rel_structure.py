from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.geographical_unit import GeographicalUnit
from generated.geographical_unit_ref import GeographicalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL UNITs.
    """

    class Meta:
        name = "geographicalUnits_RelStructure"

    geographical_unit_ref_or_geographical_unit: List[
        Union[GeographicalUnitRef, GeographicalUnit]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
