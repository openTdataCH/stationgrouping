from dataclasses import dataclass

from generated.all_transport_organisations_ref_structure import (
    AllTransportOrganisationsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOperatorsRef(AllTransportOrganisationsRefStructure):
    """
    Reference to all OPERATORs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
