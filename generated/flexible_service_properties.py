from dataclasses import dataclass

from generated.flexible_service_properties_version_structure import (
    FlexibleServicePropertiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServiceProperties(FlexibleServicePropertiesVersionStructure):
    """Additional characteristics of a FLEXIBLE SERVICE.

    A service may be partly fixed, partly flexible.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
