from dataclasses import dataclass

from generated.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractTrackedRequest(RequestStructure):
    """
    Subsititutable type for a SIRI request with requestor dteials tracked.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
