from dataclasses import dataclass

from generated.accountable_element_ref_structure import (
    AccountableElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutyPartRefStructure(AccountableElementRefStructure):
    """
    Type for Reference to a DUTY PART.
    """
