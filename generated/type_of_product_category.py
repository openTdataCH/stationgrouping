from dataclasses import dataclass

from generated.type_of_product_category_structure import (
    TypeOfProductCategoryStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProductCategory(TypeOfProductCategoryStructure):
    """
    Classification of a PRODUCT CATEGORY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
