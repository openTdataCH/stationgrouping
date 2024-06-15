from dataclasses import dataclass

from generated.travel_specification_version_structure import (
    TravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OfferedTravelSpecificationVersionStructure(
    TravelSpecificationVersionStructure
):
    """
    Type for OFFERED TRAVEL SPECIFICATION.
    """

    class Meta:
        name = "OfferedTravelSpecification_VersionStructure"
