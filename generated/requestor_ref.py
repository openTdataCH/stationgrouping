from dataclasses import dataclass

from generated.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RequestorRef(ParticipantRefStructure):
    """Reference to a requestor - Participant Code."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
