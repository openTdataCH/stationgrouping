from dataclasses import dataclass

from generated.service_exclusion_ref_structure import (
    ServiceExclusionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceExclusionRef(ServiceExclusionRefStructure):
    """
    Reference to a SERVICE EXCLUSION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
