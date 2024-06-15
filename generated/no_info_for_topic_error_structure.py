from dataclasses import dataclass

from generated.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NoInfoForTopicErrorStructure(ErrorCodeStructure):
    """Type for Error: No Info for Topic"""
