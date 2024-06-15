from dataclasses import dataclass

from generated.service_access_right_ref_structure import (
    ServiceAccessRightRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductRefStructure(ServiceAccessRightRefStructure):
    """
    Type for Reference to a FARE PRODUCT.
    """
