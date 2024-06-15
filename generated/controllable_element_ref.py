from dataclasses import dataclass

from generated.controllable_element_ref_structure import (
    ControllableElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementRef(ControllableElementRefStructure):
    """
    Reference to a CONTROLLABLE ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
