from dataclasses import dataclass

from generated.validable_element_version_structure import (
    ValidableElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElement(ValidableElementVersionStructure):
    """
    A sequence or set of FARE STRUCTURE ELEMENTs, grouped together to be validated
    in one go.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
