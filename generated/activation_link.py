from dataclasses import dataclass

from generated.activation_link_version_structure import (
    ActivationLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLink(ActivationLinkVersionStructure):
    """
    A LINK where a control process is activated when a vehicle passes it.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
