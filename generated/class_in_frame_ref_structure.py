from dataclasses import dataclass, field

from generated.class_ref_structure import ClassRefStructure
from generated.class_ref_type_enumeration import ClassRefTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassInFrameRefStructure(ClassRefStructure):
    """
    Type for a reference to the Class of a ENTITY for use in filters.

    :ivar class_ref_type: Nature of reference: Members | Member
        References | All.
    """

    class_ref_type: ClassRefTypeEnumeration = field(
        default=ClassRefTypeEnumeration.MEMBERS,
        metadata={
            "name": "classRefType",
            "type": "Attribute",
        },
    )
