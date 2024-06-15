from dataclasses import dataclass

from generated.onboard_stay_ref_structure import OnboardStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStayRef(OnboardStayRefStructure):
    """
    Reference to a ONBOARD STAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
