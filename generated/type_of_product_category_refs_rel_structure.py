from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_product_category_ref import TypeOfProductCategoryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProductCategoryRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF PRODUCT CATEGORY.
    """

    class Meta:
        name = "typeOfProductCategoryRefs_RelStructure"

    type_of_product_category_ref: List[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
