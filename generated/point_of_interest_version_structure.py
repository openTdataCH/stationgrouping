from dataclasses import dataclass, field
from typing import Optional

from generated.accesses_rel_structure import AccessesRelStructure
from generated.navigation_paths_rel_structure import (
    NavigationPathsRelStructure,
)
from generated.path_junctions_rel_structure import PathJunctionsRelStructure
from generated.point_of_interest_classifications_views_rel_structure import (
    PointOfInterestClassificationsViewsRelStructure,
)
from generated.point_of_interest_spaces_rel_structure import (
    PointOfInterestSpacesRelStructure,
)
from generated.site_path_links_rel_structure import SitePathLinksRelStructure
from generated.site_version_structure import SiteVersionStructure
from generated.topographic_place_refs_rel_structure import (
    TopographicPlaceRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVersionStructure(SiteVersionStructure):
    """
    Type for a POINT OF INTEREST.

    :ivar classifications: Membership of POI CLASSIFICATIONS.
    :ivar spaces: POINT OF INTEREST SPACEs within the POI.
    :ivar near_topographic_places: TOPOGRAPHIC PLACEs that are near to
        the POINT OF INTEREST or that contain it.
    :ivar path_links: PATH LINKs for SITE.
    :ivar path_junctions: PATH JUNCTIONs within the SITE and or between
        the SITE elsewhere.
    :ivar accesses: ACCESS links for SITE.
    :ivar navigation_paths: NAVIGATION PATHs within the SITE and or
        between the SITE elsewhere.
    """

    class Meta:
        name = "PointOfInterest_VersionStructure"

    classifications: Optional[
        PointOfInterestClassificationsViewsRelStructure
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spaces: Optional[PointOfInterestSpacesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    near_topographic_places: Optional[TopographicPlaceRefsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "nearTopographicPlaces",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
