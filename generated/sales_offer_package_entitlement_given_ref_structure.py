from dataclasses import dataclass

from generated.usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementGivenRefStructure(
    UsageParameterRefStructure
):
    """
    Type for Reference to a SALES OFFER  ENTITLEMENT GIVEN parameter.
    """
