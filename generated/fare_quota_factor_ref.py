from dataclasses import dataclass

from generated.fare_quota_factor_ref_structure import (
    FareQuotaFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactorRef(FareQuotaFactorRefStructure):
    """
    Reference to a FARE QUOTA FACTOR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
