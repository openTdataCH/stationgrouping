from dataclasses import dataclass

from generated.customer_service_version_structure import (
    CustomerServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsServiceVersionStructure(CustomerServiceVersionStructure):
    """
    Type for a COMPLAINTS SERVICE.
    """

    class Meta:
        name = "ComplaintsService_VersionStructure"
