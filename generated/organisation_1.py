from dataclasses import dataclass

from generated.organisation_version_structure import (
    OrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Organisation1(OrganisationVersionStructure):
    """
    An legally incorporated body associated with any aspect of the transport
    system.
    """

    class Meta:
        name = "Organisation"
        namespace = "http://www.netex.org.uk/netex"
