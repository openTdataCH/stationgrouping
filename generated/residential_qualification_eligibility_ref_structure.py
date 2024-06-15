from dataclasses import dataclass

from generated.customer_eligibility_ref_structure import (
    CustomerEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibilityRefStructure(
    CustomerEligibilityRefStructure
):
    """
    Type for Reference to a RESIDENTIAL QUALIFICATION ELIGIBILITY.
    """
