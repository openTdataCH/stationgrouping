from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from generated.block_ref import BlockRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.flexible_line_ref import FlexibleLineRef
from generated.journey_refs_rel_structure import JourneyRefsRelStructure
from generated.line_ref import LineRef
from generated.multilingual_string import MultilingualString
from generated.private_code import PrivateCode
from generated.train_block_ref import TrainBlockRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CourseOfJourneysVersionStructure(DataManagedObjectStructure):
    """
    Type for COURSE OF JOURNEYs.

    :ivar name: Name of COURSE OF JOURNEYs.
    :ivar description: Description of COURSE OF JOURNEYs.
    :ivar course_of_journeys_number: Numeric identifier of COURSE of
        JOURNEYS.
    :ivar private_code:
    :ivar preparation_duration: How long the run takes to prepare.
    :ivar start_time_in_block: Time at which run starts.
    :ivar start_time_day_offset: Day offset of Start time from current
        OPERATING DAY.
    :ivar finishing_duration: How long the run takes.
    :ivar train_block_ref_or_block_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar journeys: JOURNEYS making up COURSE OF JOURNEYs.
    """

    class Meta:
        name = "CourseOfJourneys_VersionStructure"

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
    course_of_journeys_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time_in_block: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTimeInBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
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
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    journeys: Optional[JourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
