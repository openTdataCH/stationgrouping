from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServiceJourneyPatternTypeEnumeration(Enum):
    """
    Allowed values for TYPE OF SERVICE JOURNEY PATTERN.

    :cvar PASSENGER:
    :cvar GARAGE_RUN_OUT: INTERCHANGE is considered a possible
        connection between journeys.
    :cvar GARAGE_RUN_IN: INTERCHANGE is advertised to public as a
        possible connection between journeys.
    :cvar TURNING_MANOEUVRE: INTERCHANGE is actively managed as a
        possible connection between journeys and passengers are informed
        of real-time alterations.
    :cvar OTHER:
    """

    PASSENGER = "passenger"
    GARAGE_RUN_OUT = "garageRunOut"
    GARAGE_RUN_IN = "garageRunIn"
    TURNING_MANOEUVRE = "turningManoeuvre"
    OTHER = "other"
