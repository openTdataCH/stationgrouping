from dataclasses import dataclass, field
from typing import Optional, Union

from generated.block_ref import BlockRef
from generated.compound_block_ref import CompoundBlockRef
from generated.compound_train_ref import CompoundTrainRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.journey_part_couple_ref import JourneyPartCoupleRef
from generated.journey_part_refs_rel_structure import (
    JourneyPartRefsRelStructure,
)
from generated.multilingual_string import MultilingualString
from generated.train_block_ref import TrainBlockRef
from generated.train_ref import TrainRef
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockPartVersionStructure(DataManagedObjectStructure):
    """
    Type for a BLOCK PART.

    :ivar name: Name of BLOCK PART.
    :ivar description: Description of BLOCK PART.
    :ivar train_block_ref_or_block_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar compound_block_ref:
    :ivar journey_part_couple_ref_or_journey_parts:
    :ivar order: Order of part within BLOCK.
    """

    class Meta:
        name = "BlockPart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    train_block_ref_or_block_ref: Optional[Union[TrainBlockRef, BlockRef]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "TrainBlockRef",
                        "type": TrainBlockRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "BlockRef",
                        "type": BlockRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    compound_block_ref: Optional[CompoundBlockRef] = field(
        default=None,
        metadata={
            "name": "CompoundBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_couple_ref_or_journey_parts: Optional[
        Union[JourneyPartCoupleRef, JourneyPartRefsRelStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyParts",
                    "type": JourneyPartRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
