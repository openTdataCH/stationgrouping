from dataclasses import dataclass

from generated.fare_contract_security_listing_ref_structure import (
    FareContractSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractSecurityListingRef(FareContractSecurityListingRefStructure):
    """
    Reference to a FARE CONTRACT SECURITY LISTING..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
