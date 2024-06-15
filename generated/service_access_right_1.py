from dataclasses import dataclass

from generated.service_access_right_version_structure import (
    ServiceAccessRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessRight1(ServiceAccessRightVersionStructure):
    """
    An immaterial marketable element dedicated to accessing some services.
    """

    class Meta:
        name = "ServiceAccessRight"
        namespace = "http://www.netex.org.uk/netex"
