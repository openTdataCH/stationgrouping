from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.entity_in_version_structure import VersionedChildStructure
from generated.handrail_enumeration import HandrailEnumeration
from generated.stair_end_structure import StairEndStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StairFlightVersionedChildStructure(VersionedChildStructure):
    """
    Flight of stairs.

    :ivar depth: Depth of Stairs.
    :ivar number_of_steps: Number of Steps on Stairs.
    :ivar step_height: Depth of an individual step.
    :ivar step_colour_contrast: Whether there is a colour contrast on
        step nosings.
    :ivar handrail_type: Type of handrail.
    :ivar handrail_height: Height of handrail from step.
    :ivar lower_handrail_height: Height of any additional lower handrail
        from step.
    :ivar top_end: Properties of top of staircase.
    :ivar bottom_end: Properties of bottom of staircase.
    :ivar continuous_handrail: Whether Handrail is continuous from
        previous stage.
    """

    class Meta:
        name = "StairFlight_VersionedChildStructure"

    depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StepHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_colour_contrast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StepColourContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_type: Optional[HandrailEnumeration] = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lower_handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    top_end: Optional[StairEndStructure] = field(
        default=None,
        metadata={
            "name": "TopEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bottom_end: Optional[StairEndStructure] = field(
        default=None,
        metadata={
            "name": "BottomEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    continuous_handrail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContinuousHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
