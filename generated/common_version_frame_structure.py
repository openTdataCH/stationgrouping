from dataclasses import dataclass

from generated.version_frame_version_structure import (
    VersionFrameVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonVersionFrameStructure(VersionFrameVersionStructure):
    """
    Type for a  COMMON FRAME.
    """

    class Meta:
        name = "Common_VersionFrameStructure"
