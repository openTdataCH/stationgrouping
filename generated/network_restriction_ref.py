from dataclasses import dataclass

from generated.network_restriction_ref_structure import (
    NetworkRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRestrictionRef(NetworkRestrictionRefStructure):
    """
    Reference to a NETWORK RESTRICTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
