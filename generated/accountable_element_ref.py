from dataclasses import dataclass

from generated.accountable_element_ref_structure import (
    AccountableElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountableElementRef(AccountableElementRefStructure):
    """
    Reference to an ACCOUNTABLE ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
