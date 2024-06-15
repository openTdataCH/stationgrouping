from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MachineReadableEnumeration(Enum):
    """
    Allowed values for ResellType.
    """

    NONE = "none"
    MAGNETIC_STRIP = "magneticStrip"
    CHIP = "chip"
    OCR = "ocr"
    BAR_CODE = "barCode"
    SHOT_CODE = "shotCode"
    NFC = "nfc"
    OTHER = "other"
