from dataclasses import dataclass

from generated.serviced_organisation_version_structure import (
    ServicedOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicedOrganisation(ServicedOrganisationVersionStructure):
    """
    ORGANISATION for which Service is provided, e.g. school college.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
