from dataclasses import dataclass

from generated.infrastructure_version_frame_structure import (
    InfrastructureVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureFrame(InfrastructureVersionFrameStructure):
    """
    A coherent set of infrastructure network description data to which the same
    VALIDITY CONDITIONs have been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
