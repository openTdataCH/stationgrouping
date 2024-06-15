from dataclasses import dataclass

from generated.travel_specification_summary_view_structure import (
    TravelSpecificationSummaryViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationSummaryView(TravelSpecificationSummaryViewStructure):
    """Summary of key aspects of TRAVEL SPECIFICATION.

    +V1.1. This data should all be derivable from the PARAMATER
    ASSIGMENTs.  v+1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
