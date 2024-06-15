from dataclasses import dataclass

from generated.all_organisations_ref_structure import (
    AllOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllTransportOrganisationsRefStructure(AllOrganisationsRefStructure):
    """
    Type for a reference to  all TRANSPORT ORGANISATIONs.
    """
