from dataclasses import dataclass

from generated.pricing_service_versioned_structure import (
    PricingServiceVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingService(PricingServiceVersionedStructure):
    """
    A web service used to provide prices dynamically at time of booking or
    purchase.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
