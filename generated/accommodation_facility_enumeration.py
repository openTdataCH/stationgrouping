from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccommodationFacilityEnumeration(Enum):
    """
    Allowed values for Accommodation Facility.
    """

    UNKNOWN = "unknown"
    SEATING = "seating"
    SLEEPER = "sleeper"
    SINGLE_SLEEPER = "singleSleeper"
    DOUBLE_SLEEPER = "doubleSleeper"
    SPECIAL_SLEEPER = "specialSleeper"
    COUCHETTE = "couchette"
    SINGLE_COUCHETTE = "singleCouchette"
    DOUBLE_COUCHETTE = "doubleCouchette"
    SPECIAL_SEATING = "specialSeating"
    RECLINING_SEATS = "recliningSeats"
    BABY_COMPARTMENT = "babyCompartment"
    FAMILY_CARRIAGE = "familyCarriage"
    RECREATION_AREA = "recreationArea"
    PANORAMA_COACH = "panoramaCoach"
    PULLMAN_COACH = "pullmanCoach"
    STANDING = "standing"
