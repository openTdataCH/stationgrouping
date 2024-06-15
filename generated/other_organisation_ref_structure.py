from dataclasses import dataclass

from generated.organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherOrganisationRefStructure(OrganisationRefStructure):
    """
    Type for a reference to an OTHER ORGANISATION.
    """
