from dataclasses import dataclass

from generated.abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequest(AbstractRequestStructure):
    """
    Subsititutable type for a timestamped SIRI request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
