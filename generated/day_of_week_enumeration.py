from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DayOfWeekEnumeration(Enum):
    """
    Allowed values for Day of the Week.
    """

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    EVERYDAY = "Everyday"
    WEEKDAYS = "Weekdays"
    WEEKEND = "Weekend"
    NONE = "none"
