from dataclasses import dataclass

from generated.point_of_interest_version_structure import (
    PointOfInterestVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterest(PointOfInterestVersionStructure):
    """
    A type of SITE to or through which passengers may wish to navigate as part of
    their journey and which is modelled in detail by journey planners.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
