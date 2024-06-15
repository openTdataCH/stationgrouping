from dataclasses import dataclass

from generated.network_frame_topic_structure import NetworkFrameTopicStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkFrameTopic(NetworkFrameTopicStructure):
    """Network Object filter  Return Network Objects that match these values.

    Values are ANDed.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
