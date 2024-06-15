from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.control_centre import ControlCentre
from generated.control_centre_ref import ControlCentreRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControlCentresRelStructure(ContainmentAggregationStructure):
    """
    A list of CONTROL CENTREs.
    """

    class Meta:
        name = "ControlCentres_RelStructure"

    control_centre_ref_or_control_centre: List[
        Union[ControlCentreRef, ControlCentre]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
