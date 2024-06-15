from dataclasses import dataclass

from generated.travel_specification_ref_structure import (
    TravelSpecificationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecificationRefStructure(
    TravelSpecificationRefStructure
):
    """
    Type for Reference to a REQUESTED TRAVEL SPECIFICATION.
    """
