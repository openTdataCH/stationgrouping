from dataclasses import dataclass

from generated.modal_link_ref_by_value_structure import (
    ModalLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModalLinkRefByValue(ModalLinkRefByValueStructure):
    """
    Reference to a LINK using its end values.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
