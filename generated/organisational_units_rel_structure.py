from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.organisational_unit import OrganisationalUnit
from generated.organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ORGANISATIONAL UNITs.
    """

    class Meta:
        name = "organisationalUnits_RelStructure"

    organisational_unit_ref_or_organisational_unit: List[
        Union[OrganisationalUnitRef, OrganisationalUnit]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
