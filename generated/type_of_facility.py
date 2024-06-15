from dataclasses import dataclass, field
from typing import Any

from generated.type_of_facility_version_structure import (
    TypeOfFacilityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFacility(TypeOfFacilityVersionStructure):
    """A classification of FACILITYs expressing their general functionalities and
    local functional characteristics specific to the operator.

    Types of FACILITYs like e.g. throw-away ticket, throw-away ticket
    unit, value card, electronic purse allowing access, public transport
    credit card etc. may be used to define these categories.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
