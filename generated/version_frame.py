from dataclasses import dataclass

from generated.version_frame_version_structure import (
    VersionFrameVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionFrame(VersionFrameVersionStructure):
    """A set of VERSIONS referring to a same DATA SYSTEM and belonging to the same
    TYPE OF FRAME.

    A FRAME may be restricted by VALIDITY CONDITIONs.  Container for a
    coherent set of versions of objects.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
