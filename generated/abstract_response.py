from dataclasses import dataclass

from generated.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractResponse(ResponseStructure):
    """
    Subsititutable type for a SIRI response.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
