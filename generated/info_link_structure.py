from dataclasses import dataclass, field
from typing import List

from generated.type_of_infolink_enumeration import TypeOfInfolinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfoLinkStructure:
    """
    Type for Info LinK.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_of_info_link: List[TypeOfInfolinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        },
    )
