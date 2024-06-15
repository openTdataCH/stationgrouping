from dataclasses import dataclass

from generated.onboard_stay_versioned_chlld_structure import (
    OnboardStayVersionedChlldStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStay(OnboardStayVersionedChlldStructure):
    """
    Boarding permission to board early or stay on board late.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
