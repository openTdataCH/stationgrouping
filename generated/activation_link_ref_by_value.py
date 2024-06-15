from dataclasses import dataclass

from generated.activation_link_ref_by_value_structure import (
    ActivationLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLinkRefByValue(ActivationLinkRefByValueStructure):
    """
    Reference to a ACTIVATION LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
