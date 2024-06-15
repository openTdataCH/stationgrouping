from dataclasses import dataclass

from generated.sales_transaction_ref_structure import (
    SalesTransactionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionRef(SalesTransactionRefStructure):
    """
    Reference to a SALES TRANSACTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
