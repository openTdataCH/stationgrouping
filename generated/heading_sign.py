from dataclasses import dataclass

from generated.heading_sign_structure import HeadingSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadingSign(HeadingSignStructure):
    """
    Specialisation of SIGN EQUIPMENT for headings providing information like
    direction name, line name, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
