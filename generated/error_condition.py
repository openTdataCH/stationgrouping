from dataclasses import dataclass

from generated.error_condition_structure import ErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCondition(ErrorConditionStructure):
    """
    Description of error or warning condition associated with response.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
