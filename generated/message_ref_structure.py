from dataclasses import dataclass

from generated.message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MessageRefStructure(MessageQualifierStructure):
    """
    Type for message ref.
    """
