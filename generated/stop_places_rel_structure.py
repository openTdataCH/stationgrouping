from dataclasses import dataclass, field
from typing import Optional, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.stop_place import StopPlace
from generated.stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of STOP PLACEs.
    """

    class Meta:
        name = "stopPlaces_RelStructure"

    stop_place_ref_or_stop_place: Optional[Union[StopPlaceRef, StopPlace]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "StopPlaceRef",
                        "type": StopPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlace",
                        "type": StopPlace,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
