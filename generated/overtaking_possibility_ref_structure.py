from dataclasses import dataclass

from generated.network_restriction_ref_structure import (
    NetworkRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OvertakingPossibilityRefStructure(NetworkRestrictionRefStructure):
    """
    Type for Reference to  an  OVERTAKING POSSIBILITY.
    """
