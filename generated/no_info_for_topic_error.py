from dataclasses import dataclass

from generated.no_info_for_topic_error_structure import (
    NoInfoForTopicErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NoInfoForTopicError(NoInfoForTopicErrorStructure):
    """Error: Valid request was made but service does not hold any data for the requested topic. expression."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
