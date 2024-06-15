from dataclasses import dataclass

from generated.common_version_frame_structure import (
    CommonVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonFrame(CommonVersionFrameStructure):
    """
    Abstract supertype for explicit VERSION FRAMEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
