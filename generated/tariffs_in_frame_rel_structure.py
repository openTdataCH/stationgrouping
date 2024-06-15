from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.tariff import Tariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TARIFF.
    """

    class Meta:
        name = "tariffsInFrame_RelStructure"

    tariff: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
