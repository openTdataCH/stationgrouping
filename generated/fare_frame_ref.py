from dataclasses import dataclass

from generated.fare_frame_ref_structure import FareFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareFrameRef(FareFrameRefStructure):
    """
    Reference to a FARE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
