from dataclasses import dataclass

from generated.month_validity_offset_versioned_structure import (
    MonthValidityOffsetVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonthValidityOffset(MonthValidityOffsetVersionedStructure):
    """
    Days before (negative) or after (positive)  the start of the month that a
    product with a calendar period driven activation becomes valid.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
