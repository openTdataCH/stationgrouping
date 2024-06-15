from dataclasses import dataclass

from generated.type_of_validity_value_structure import (
    TypeOfValidityValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfValidity(TypeOfValidityValueStructure):
    """A classification of the validity of TYPEs OF FRAME.

    E.g. frames for schedules designed for DAY TYPEs, for specific
    OPERATING DAYs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
