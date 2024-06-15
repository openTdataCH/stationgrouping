from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassengerInformationEquipmentEnumeration(Enum):
    """
    Allowed values for Passenger Information Equipment.
    """

    TIMETABLE_POSTER = "timetablePoster"
    FARE_INFORMATION = "fareInformation"
    LINE_NETWORK_PLAN = "lineNetworkPlan"
    LINE_TIMETABLE = "lineTimetable"
    STOP_TIMETABLE = "stopTimetable"
    JOURNEY_PLANNING = "journeyPlanning"
    INTERACTIVE_KIOSK = "interactiveKiosk"
    INFORMATION_DESK = "informationDesk"
    NETWORK_STATUS = "networkStatus"
    REAL_TIME_DISRUPTIONS = "realTimeDisruptions"
    REAL_TIME_DEPARTURES = "realTimeDepartures"
    OTHER = "other"
