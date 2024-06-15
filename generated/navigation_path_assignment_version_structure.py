from dataclasses import dataclass, field
from typing import Optional, Union

from generated.connection_ref import ConnectionRef
from generated.default_connection_ref import DefaultConnectionRef
from generated.navigation_path_ref import NavigationPathRef
from generated.parking_ref import ParkingRef
from generated.point_of_interest_ref import PointOfInterestRef
from generated.service_site_ref import ServiceSiteRef
from generated.site_connection_ref import SiteConnectionRef
from generated.site_ref import SiteRef
from generated.stop_assignment_version_structure import (
    StopAssignmentVersionStructure,
)
from generated.stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a NAVIGATION PATH ASSIGNMENT.
    """

    class Meta:
        name = "NavigationPathAssignment_VersionStructure"

    default_connection_ref_or_site_connection_ref_or_connection_ref: Optional[
        Union[DefaultConnectionRef, SiteConnectionRef, ConnectionRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: Optional[
        Union[
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
