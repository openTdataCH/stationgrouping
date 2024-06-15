from dataclasses import dataclass

from generated.point_of_interest_component_version_structure import (
    PointOfInterestComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestComponent(PointOfInterestComponentVersionStructure):
    """
    A part of the physical structure of a POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
