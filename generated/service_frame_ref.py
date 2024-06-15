from dataclasses import dataclass

from generated.service_frame_ref_structure import ServiceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFrameRef(ServiceFrameRefStructure):
    """
    Reference to a SERVICE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
