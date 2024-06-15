from dataclasses import dataclass, field
from typing import Optional

from generated.other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)
from generated.service_calendar_ref import ServiceCalendarRef
from generated.serviced_organisation_type_enumeration import (
    ServicedOrganisationTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicedOrganisationVersionStructure(OtherOrganisationVersionStructure):
    """
    Type for an OTHER ORGANISATION.

    :ivar service_calendar_ref:
    :ivar serviced_organisation_type: Type of serviced ORGANISATION.
    """

    class Meta:
        name = "ServicedOrganisation_VersionStructure"

    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    serviced_organisation_type: Optional[
        ServicedOrganisationTypeEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
