from dataclasses import dataclass

from generated.infrastructure_link_restriction_version_structure import (
    InfrastructureLinkRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkRestriction(
    InfrastructureLinkRestrictionVersionStructure
):
    """
    A NETWORK RESTRICTION on movement between any two network links.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
