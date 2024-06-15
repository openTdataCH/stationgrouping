from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BooleanOperatorEnumeration(Enum):
    """
    Allowed values for Boolean operations.

    :cvar AND: Successive elements are logically ANDed together;
        comparison must satisfy all specified values.
    :cvar OR: Successive elements are logically ORed together;
        comparison must satisfy at least one  specified value.
    :cvar NOT: Specified elements  must be different from the given
        value.
    :cvar XOR: Successive elements are logically ORed together;
        comparison must satisfy only one  specified value.
    """

    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    XOR = "XOR"
