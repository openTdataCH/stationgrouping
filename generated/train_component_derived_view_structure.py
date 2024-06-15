from dataclasses import dataclass, field
from typing import Optional

from generated.derived_view_structure import DerivedViewStructure
from generated.fare_classes import FareClasses
from generated.multilingual_string import MultilingualString
from generated.train_component_ref import TrainComponentRef
from generated.train_element_ref import TrainElementRef
from generated.train_element_type_enumeration import (
    TrainElementTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentDerivedViewStructure(DerivedViewStructure):
    """
    Type for TRAIN COMPONENT VIEW.

    :ivar train_component_ref:
    :ivar label: Label for TRAIN COMPONENT.
    :ivar description: Description of TRAIN COMPONENT.
    :ivar train_element_ref: Reference to a TRAIN ELEMENT.
    :ivar fare_classes:
    :ivar train_element_type: Type of TRAIN ELEMENT.
    :ivar order: Order of TRAIN COMPONENT within TRAIN.
    """

    class Meta:
        name = "TrainComponent_DerivedViewStructure"

    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: Optional[FareClasses] = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_type: Optional[TrainElementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
