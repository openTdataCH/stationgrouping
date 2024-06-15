from dataclasses import dataclass

from generated.usage_validity_period_version_structure import (
    UsageValidityPeriodVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageValidityPeriod(UsageValidityPeriodVersionStructure):
    """A time limitation for validity of a FARE PRODUCT or a SALES OFFER PACKAGE.

    It may be composed of a standard duration (e.g. 3 days, 1 month)
    and/or fixed start/end dates and times.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
