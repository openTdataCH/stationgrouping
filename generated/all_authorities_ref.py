from dataclasses import dataclass

from generated.all_transport_organisations_ref_structure import (
    AllTransportOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllAuthoritiesRef(AllTransportOrganisationsRefStructure):
    """
    Reference to all AUTHORITIies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
