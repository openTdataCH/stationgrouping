from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class WeekOfMonthEnumeration(Enum):
    """
    Allowed values for Week of the Month.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    EVERY_WEEK = "EveryWeek"
