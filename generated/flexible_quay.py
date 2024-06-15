from dataclasses import dataclass

from generated.flexible_quay_version_structure import (
    FlexibleQuayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleQuay(FlexibleQuayVersionStructure):
    """
    A ZONE of physical access to public transport vehicles such as a platform.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
