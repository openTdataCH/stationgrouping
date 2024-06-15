from dataclasses import dataclass

from generated.type_of_product_category_ref_structure import (
    TypeOfProductCategoryRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProductCategoryRef(TypeOfProductCategoryRefStructure):
    """Reference to a TYPE OF PRODUCT CATEGORY.

    Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037
    Characteristic description code.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
