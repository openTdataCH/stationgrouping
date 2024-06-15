from dataclasses import dataclass

from generated.travel_specification_version_structure import (
    TravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecificationVersionStructure(
    TravelSpecificationVersionStructure
):
    """
    Type for REQUESTED TRAVEL SPECIFICATION.
    """

    class Meta:
        name = "RequestedTravelSpecification_VersionStructure"
