from dataclasses import dataclass

from generated.version_frame_ref_structure import VersionFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionFrameRef(VersionFrameRefStructure):
    """
    Reference to a VERSION FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
