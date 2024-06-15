from dataclasses import dataclass

from generated.infrastructure_link_ref_structure import (
    InfrastructureLinkRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkRef(InfrastructureLinkRefStructure):
    """
    Reference to an INFRASTRUCTURE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
