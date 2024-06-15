from dataclasses import dataclass

from generated.version_frame_ref_structure import VersionFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositeFrameRefStructure(VersionFrameRefStructure):
    """
    Type for a reference to a COMPOSITE FRAME.
    """
