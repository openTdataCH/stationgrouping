from dataclasses import dataclass

from generated.requested_travel_specification_version_structure import (
    RequestedTravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecification(
    RequestedTravelSpecificationVersionStructure
):
    """
    The recording of a specification by a customer of parameters giving details of
    an intended consumption (e.g. origin and destination of a travel).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
