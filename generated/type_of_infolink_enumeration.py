from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfInfolinkEnumeration(Enum):
    """
    Enumeration of Uses of language.
    """

    CONTACT = "contact"
    RESOURCE = "resource"
    INFO = "info"
    IMAGE = "image"
    DOCUMENT = "document"
    TIMETABLE_DOCUMENT = "timetableDocument"
    FARE_SHEET = "fareSheet"
    DATA_LICENCE = "dataLicence"
    MAP = "map"
    ICON = "icon"
    OTHER = "other"
