from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServicedOrganisationTypeEnumeration(Enum):
    """
    Allowed values for SERVICED ORGANISATION type.
    """

    SCHOOL = "school"
    COLLEGE = "college"
    UNIVERSITY = "university"
    MILITARY_BASE = "militaryBase"
    WORKS = "works"
    RETAIIL_CENTRE = "retaiilCentre"
    HOSPITAL = "hospital"
    GOVERNMENT_OFFICE = "governmentOffice"
    OTHER = "other"
