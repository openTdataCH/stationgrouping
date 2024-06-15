from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AllModesEnumeration(Enum):
    """Allowed values for r MODES: TPEG pti_table 01.

    :cvar ALL:
    :cvar UNKNOWN:
    :cvar AIR:
    :cvar BUS:
    :cvar TROLLEY_BUS:
    :cvar TRAM:
    :cvar COACH:
    :cvar RAIL:
    :cvar INTERCITY_RAIL:
    :cvar URBAN_RAIL:
    :cvar METRO:
    :cvar WATER:
    :cvar CABLEWAY:
    :cvar FUNICULAR:
    :cvar LIFT:
    :cvar SNOW_AND_ICE:
    :cvar TAXI:
    :cvar SELF_DRIVE: See pti12_x.
    :cvar FOOT:
    :cvar BICYCLE:
    :cvar MOTORCYCLE:
    :cvar CAR:
    :cvar SHUTTLE:
    """

    ALL = "all"
    UNKNOWN = "unknown"
    AIR = "air"
    BUS = "bus"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITY_RAIL = "intercityRail"
    URBAN_RAIL = "urbanRail"
    METRO = "metro"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    LIFT = "lift"
    SNOW_AND_ICE = "snowAndIce"
    TAXI = "taxi"
    SELF_DRIVE = "selfDrive"
    FOOT = "foot"
    BICYCLE = "bicycle"
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    SHUTTLE = "shuttle"
