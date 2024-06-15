from dataclasses import dataclass, field

from generated.request_timestamp import RequestTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequestStructure:
    """
    Type for General SIRI Request.
    """

    request_timestamp: RequestTimestamp = field(
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
