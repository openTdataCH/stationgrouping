from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionQualifierStructure:
    """
    Type Unique identifier of Subscription within Participant.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
