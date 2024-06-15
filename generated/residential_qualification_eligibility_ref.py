from dataclasses import dataclass

from generated.residential_qualification_eligibility_ref_structure import (
    ResidentialQualificationEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibilityRef(
    ResidentialQualificationEligibilityRefStructure
):
    """
    Reference to a RESIDENTIAL QUALIFICATION ELIGIBILIT..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
