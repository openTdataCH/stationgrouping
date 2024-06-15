from dataclasses import dataclass

from generated.network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRestriction(NetworkRestrictionVersionStructure):
    """
    A constraint on use of a network of INFRASTRUCTURE POINTs and INFRASTUCTURE
    LINKs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
