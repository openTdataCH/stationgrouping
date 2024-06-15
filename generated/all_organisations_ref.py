from dataclasses import dataclass

from generated.all_organisations_ref_structure import (
    AllOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOrganisationsRef(AllOrganisationsRefStructure):
    """
    Reference to all ORGANISATIONs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
