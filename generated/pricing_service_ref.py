from dataclasses import dataclass

from generated.pricing_service_ref_structure import PricingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingServiceRef(PricingServiceRefStructure):
    """
    Reference to a PRICING SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
