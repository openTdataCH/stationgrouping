from dataclasses import dataclass

from generated.topic_structure import TopicStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Topic(TopicStructure):
    """
    Abstract Topic Filter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
