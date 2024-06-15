from dataclasses import dataclass

from generated.service_version_frame_structure import (
    ServiceVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFrame(ServiceVersionFrameStructure):
    """
    A coherent set of Service data to which the same frame VALIDITY CONDITIONs have
    been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
