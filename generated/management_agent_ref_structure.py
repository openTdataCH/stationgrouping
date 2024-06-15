from dataclasses import dataclass

from generated.other_organisation_ref_structure import (
    OtherOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgentRefStructure(OtherOrganisationRefStructure):
    """
    Type for a reference to a MANAGEMENT AGENT.
    """
