from dataclasses import dataclass, field

from generated.abstract_item_structure import AbstractItemStructure
from generated.item_ref_structure import ItemRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequiredReferencingItemStructure(AbstractItemStructure):
    """
    Type for an Activity that references a previous Activity.

    :ivar item_ref: Reference to an Activity Element of  a delivery.
    """

    item_ref: ItemRefStructure = field(
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
