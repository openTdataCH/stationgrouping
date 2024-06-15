from dataclasses import dataclass

from generated.composite_frame_ref_structure import CompositeFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositeFrameRef(CompositeFrameRefStructure):
    """
    Reference to a COMPOSITE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
