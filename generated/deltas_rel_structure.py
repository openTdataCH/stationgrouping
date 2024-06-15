from dataclasses import dataclass, field
from typing import List

from generated.delta import Delta

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltasRelStructure:
    """
    A collection of one or more DELTAs.
    """

    class Meta:
        name = "deltas_RelStructure"

    delta: List[Delta] = field(
        default_factory=list,
        metadata={
            "name": "Delta",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
