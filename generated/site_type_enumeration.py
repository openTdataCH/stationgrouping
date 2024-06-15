from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SiteTypeEnumeration(Enum):
    """
    Types of SITE.
    """

    SCHOOL = "school"
    UNIVERSITY = "university"
    WORKS = "works"
    OFFICE = "office"
    MILITARY_BASE = "militaryBase"
    RETAIL = "retail"
    OTHER = "other"
