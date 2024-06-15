from dataclasses import dataclass

from generated.overtaking_possibility_ref_structure import (
    OvertakingPossibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OvertakingPossibilityRef(OvertakingPossibilityRefStructure):
    """
    Reference to an  OVERTAKING POSSIBILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
