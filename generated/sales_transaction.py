from dataclasses import dataclass, field
from typing import Any

from generated.sales_transaction_version_structure import (
    SalesTransactionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransaction(SalesTransactionVersionStructure):
    """
    A SALE OF a FIXED PACKAGE or a SALE OF a RELOADABLE PACKAGE.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
