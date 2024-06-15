from dataclasses import dataclass

from generated.journey_accounting_ref_structure import (
    JourneyAccountingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyAccountingRef(JourneyAccountingRefStructure):
    """
    Reference to a JOURNEY ACCOUNTING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
