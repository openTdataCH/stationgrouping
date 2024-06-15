from dataclasses import dataclass

from generated.serviced_organisation_ref_structure import (
    ServicedOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicedOrganisationRef(ServicedOrganisationRefStructure):
    """
    Reference to a SERVICED ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
