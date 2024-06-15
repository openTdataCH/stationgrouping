from dataclasses import dataclass, field
from typing import Optional

from generated.error_code_structure import ErrorCodeStructure
from generated.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    """Type for Error: Unknown Participant. +SIRI v2.0

    :ivar participant_ref: Reference to  Participant who is unknown. +
        SIRI v2.0
    """

    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
