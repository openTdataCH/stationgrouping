from dataclasses import dataclass

from generated.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCode(ErrorCodeStructure):
    """
    Subsititutable type for a SIRI Error code.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
