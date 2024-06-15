from dataclasses import dataclass

from generated.abstract_subscription_structure import (
    AbstractSubscriptionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceSubscriptionRequest(
    AbstractSubscriptionStructure
):
    """
    Subsititutable type for a SIRI Functional Service subscription request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
