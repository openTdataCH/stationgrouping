from dataclasses import dataclass

from generated.other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgentVersionStructure(OtherOrganisationVersionStructure):
    """
    Type for an OTHER ORGANISATION.
    """

    class Meta:
        name = "ManagementAgent_VersionStructure"
