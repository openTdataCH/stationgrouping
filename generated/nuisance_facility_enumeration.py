from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NuisanceFacilityEnumeration(Enum):
    """Allowed values for Nuisance Facility: TPEG pti_table 23."""

    UNKNOWN = "unknown"
    SMOKING = "smoking"
    NO_SMOKING = "noSmoking"
    FAMILY_AREA = "familyArea"
    CHILDFREE_AREA = "childfreeArea"
    NO_ANIMALS = "noAnimals"
    BREASTFEEDING_FRIENDLY = "breastfeedingFriendly"
    MOBILE_PHONE_USE_ZONE = "mobilePhoneUseZone"
    MOBILE_PHONE_FREE_ZONE = "mobilePhoneFreeZone"
