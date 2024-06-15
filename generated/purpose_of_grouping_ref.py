from dataclasses import dataclass

from generated.purpose_of_grouping_ref_structure import (
    PurposeOfGroupingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfGroupingRef(PurposeOfGroupingRefStructure):
    """
    Reference to a PURPOSE OF GROUPING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
