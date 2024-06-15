from dataclasses import dataclass, field
from typing import Any

from generated.accountable_element_structure import AccountableElementStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountableElement(AccountableElementStructure):
    """A period of a driver's DUTY during which (s)he is continuously working
    without a BREAK.

    PAUSEs during which (the)he remains responsible for the vehicle may
    be included.

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
