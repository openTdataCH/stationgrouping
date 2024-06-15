from dataclasses import dataclass, field
from typing import Optional

from generated.block_version_structure import BlockVersionStructure
from generated.coupled_journeys_rel_structure import (
    CoupledJourneysRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockVersionStructure(BlockVersionStructure):
    """
    Type for TRAIN BLOCK.

    :ivar coupled_journeys: JOURNEYS making up BLOCK.
    """

    class Meta:
        name = "TrainBlock_VersionStructure"

    coupled_journeys: Optional[CoupledJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "coupledJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
