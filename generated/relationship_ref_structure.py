from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelationshipRefStructure:
    """
    Type for a reference to a Relationship.

    :ivar value:
    :ivar name_of_class: Name of referenced Class.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_class: str = field(
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
            "required": True,
        }
    )
