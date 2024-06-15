from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CompressionMethodEnumeration(Enum):
    """
    Enumeration of compression usage.
    """

    GZIP = "gzip"
    NONE = "none"
    OTHER = "other"
