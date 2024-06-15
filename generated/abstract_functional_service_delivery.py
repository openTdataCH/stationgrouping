from dataclasses import dataclass

from generated.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceDelivery(AbstractServiceDeliveryStructure):
    """
    Subsititutable type for a SIRI Functional Service Deivery.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
