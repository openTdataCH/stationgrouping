from dataclasses import dataclass

from generated.class_in_frame_ref_structure import ClassInFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassInFrameRef(ClassInFrameRefStructure):
    """
    Class and nature of data inclusion.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
