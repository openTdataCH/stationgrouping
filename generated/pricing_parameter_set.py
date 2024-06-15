from dataclasses import dataclass

from generated.pricing_parameter_set_versioned_structure import (
    PricingParameterSetVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingParameterSet(PricingParameterSetVersionedStructure):
    """
    Parameters  governing the calculation of fares.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
