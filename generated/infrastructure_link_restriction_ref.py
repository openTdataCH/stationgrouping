from dataclasses import dataclass

from generated.infrastructure_link_restriction_ref_structure import (
    InfrastructureLinkRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkRestrictionRef(
    InfrastructureLinkRestrictionRefStructure
):
    """
    Reference to an INFRASTRUCTURE LINK RESTRICTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
