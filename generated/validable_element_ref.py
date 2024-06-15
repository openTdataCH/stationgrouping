from dataclasses import dataclass

from generated.validable_element_ref_structure import (
    ValidableElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementRef(ValidableElementRefStructure):
    """
    Reference to a VALIDABLE ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
