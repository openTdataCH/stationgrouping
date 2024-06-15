from dataclasses import dataclass

from generated.type_of_frame_ref_structure import TypeOfFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFrameRef(TypeOfFrameRefStructure):
    """
    Reference to a TYPE OF VERSION FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
