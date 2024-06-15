from dataclasses import dataclass, field

from generated.response_timestamp import ResponseTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ResponseStructure:
    """
    General Type for General SIRI Response.
    """

    response_timestamp: ResponseTimestamp = field(
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
