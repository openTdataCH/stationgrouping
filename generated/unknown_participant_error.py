from dataclasses import dataclass

from generated.unknown_participant_error_structure import (
    UnknownParticipantErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownParticipantError(UnknownParticipantErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. +SIRI v2.0"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
