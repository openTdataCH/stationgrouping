from dataclasses import dataclass

from generated.offered_travel_specification_ref_structure import (
    OfferedTravelSpecificationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OfferedTravelSpecificationRef(OfferedTravelSpecificationRefStructure):
    """
    Reference to an OFFERED TRAVEL SPECIFICATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
