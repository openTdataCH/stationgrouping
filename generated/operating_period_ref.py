from dataclasses import dataclass

from generated.operating_period_ref_structure import (
    OperatingPeriodRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingPeriodRef(OperatingPeriodRefStructure):
    """
    Reference to an OPERATING PERIOD.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
