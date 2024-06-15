from dataclasses import dataclass

from generated.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OtherErrorStructure(ErrorCodeStructure):
    """
    Type for error.
    """
