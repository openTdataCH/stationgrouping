from dataclasses import dataclass

from generated.pricing_parameter_set_ref_structure import (
    PricingParameterSetRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingParameterSetRef(PricingParameterSetRefStructure):
    """
    Reference to a PRICING PARAMETERS.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
