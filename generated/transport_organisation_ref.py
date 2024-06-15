from dataclasses import dataclass

from generated.organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportOrganisationRef(OrganisationRefStructure):
    """
    Reference to an  TRANSPORT ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
