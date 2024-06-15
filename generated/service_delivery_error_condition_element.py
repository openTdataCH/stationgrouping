from dataclasses import dataclass

from generated.service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceDeliveryErrorConditionElement(
    ServiceDeliveryErrorConditionStructure
):
    """
    Element fror an erroc condition for use in WSDL.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
