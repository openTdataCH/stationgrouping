from dataclasses import dataclass, field
from typing import Optional

from generated.fare_product_prices_rel_structure import (
    FareProductPricesRelStructure,
)
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.service_access_right_version_structure import (
    ServiceAccessRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProductVersionStructure(ServiceAccessRightVersionStructure):
    """
    Type for ENTITLEMENT PRODUCT.

    :ivar general_organisation_ref:
    :ivar prices: Prices for ENTITLEMENT PRODUCT.
    """

    class Meta:
        name = "EntitlementProduct_VersionStructure"

    general_organisation_ref: Optional[GeneralOrganisationRef] = field(
        default=None,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[FareProductPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
