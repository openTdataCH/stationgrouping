from dataclasses import dataclass, field

from generated.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkRefByValueStructure(LinkRefByValueStructure):
    """
    Type for a reference to a PATH LINK BY VALUE.

    :ivar name_of_point_ref_class: Class of POINT referenced by LINK.
    """

    name_of_point_ref_class: str = field(
        init=False,
        default="PathPoint",
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )
