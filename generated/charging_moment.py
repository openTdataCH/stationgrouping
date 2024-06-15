from dataclasses import dataclass

from generated.charging_moment_value_structure import (
    ChargingMomentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMoment(ChargingMomentValueStructure):
    """A classification of FARE PRODUCTs according to the payment method and the account location: pre-payment with cancellation (throw-away), pre-payment with debit on a value card, pre-payment without consumption registration (pass), post-payment etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
