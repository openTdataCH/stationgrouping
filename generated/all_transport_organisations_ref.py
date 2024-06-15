from dataclasses import dataclass

from generated.all_transport_organisations_ref_structure import (
    AllTransportOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllTransportOrganisationsRef(AllTransportOrganisationsRefStructure):
    """
    Reference to all  TRANSPORT ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
