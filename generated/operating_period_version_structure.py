from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.holiday_type_enumeration import HolidayTypeEnumeration
from generated.multilingual_string import MultilingualString
from generated.operating_day_ref_structure import OperatingDayRefStructure
from generated.season_enumeration import SeasonEnumeration
from generated.service_calendar_ref import ServiceCalendarRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingPeriodVersionStructure(DataManagedObjectStructure):
    """
    Type for an OPERATING PERIOD.

    :ivar service_calendar_ref: Reference to parent Calendar. If given
        by context, does not need to be given.
    :ivar name: Name of  OPERATING PERIOD.
    :ivar short_name: Short Name  of  OPERATING PERIOD.
    :ivar from_operating_day_ref_or_from_date:
    :ivar to_operating_day_ref_or_to_date:
    :ivar holiday_type: Whether days of OPERATING PERIOD are all in a
        holiday.
    :ivar season: Season in which OPERATING PERIOD falls.
    """

    class Meta:
        name = "OperatingPeriod_VersionStructure"

    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_operating_day_ref_or_from_date: Optional[
        Union[OperatingDayRefStructure, XmlDateTime]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FromOperatingDayRef",
                    "type": OperatingDayRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromDate",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    to_operating_day_ref_or_to_date: Optional[
        Union[OperatingDayRefStructure, XmlDateTime]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ToOperatingDayRef",
                    "type": OperatingDayRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToDate",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    holiday_type: List[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    season: List[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
        },
    )
