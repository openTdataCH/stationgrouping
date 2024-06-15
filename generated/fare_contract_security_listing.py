from dataclasses import dataclass

from generated.fare_contract_security_listing_versioned_child_structure import (
    FareContractSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractSecurityListing(
    FareContractSecurityListingVersionedChildStructure
):
    """
    A listing of a FARE CONTRACT on a SECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
