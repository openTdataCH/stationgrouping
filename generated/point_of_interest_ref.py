from dataclasses import dataclass

from generated.point_of_interest_ref_structure import (
    PointOfInterestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestRef(PointOfInterestRefStructure):
    """
    Reference to a POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
