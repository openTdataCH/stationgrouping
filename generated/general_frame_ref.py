from dataclasses import dataclass

from generated.general_frame_ref_structure import GeneralFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameRef(GeneralFrameRefStructure):
    """
    Reference to a GENERAL FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
