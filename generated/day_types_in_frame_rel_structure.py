from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entity_in_version_structure import (
    DayType,
    FareDayType,
    OrganisationDayType,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DAY TYPEs.
    """

    class Meta:
        name = "dayTypesInFrame_RelStructure"

    fare_day_type_or_organisation_day_type_or_day_type: List[
        Union[FareDayType, OrganisationDayType, DayType]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
