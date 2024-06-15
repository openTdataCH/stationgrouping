from dataclasses import dataclass

from generated.series_constraint_price_ref_structure import (
    SeriesConstraintPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintPriceRef(SeriesConstraintPriceRefStructure):
    """
    Reference to a SERIES CONSTRAINT PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
