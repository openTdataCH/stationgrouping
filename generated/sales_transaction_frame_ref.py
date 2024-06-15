from dataclasses import dataclass

from generated.sales_transaction_frame_ref_structure import (
    SalesTransactionFrameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionFrameRef(SalesTransactionFrameRefStructure):
    """
    Reference to a SALES TRANSACTION FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
