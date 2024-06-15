from dataclasses import dataclass

from generated.error_condition_element_structure import (
    ErrorConditionElementStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorConditionElement(ErrorConditionElementStructure):
    """
    Element fror an erroc condition  (for use in WSDL.)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
