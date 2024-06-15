from dataclasses import dataclass

from generated.companion_profile_version_structure import (
    CompanionProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompanionProfile(CompanionProfileVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
