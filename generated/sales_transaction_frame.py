from dataclasses import dataclass

from generated.sales_transaction_frame_version_frame_structure import (
    SalesTransactionFrameVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionFrame(SalesTransactionFrameVersionFrameStructure):
    """
    A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs
    have been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
