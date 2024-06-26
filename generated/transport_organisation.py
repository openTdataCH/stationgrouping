from dataclasses import dataclass

from generated.organisation_version_structure import (
    OrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportOrganisation(OrganisationVersionStructure):
    """
    A company  providing public transport services.
    """

    class Meta:
        name = "TransportOrganisation_"
        namespace = "http://www.netex.org.uk/netex"
