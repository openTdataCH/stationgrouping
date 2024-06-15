from dataclasses import dataclass, field
from typing import Optional, Union

from generated.group_of_operators import GroupOfOperators
from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.multilingual_string import MultilingualString
from generated.timing_point_version_structure import (
    TimingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointValueStructure(TimingPointVersionStructure):
    """
    Type for a BORDER POINT.

    :ivar short_name: Short Name of BORDER POINT.
    :ivar description: Description of BORDER POINT.
    :ivar group_of_operators_ref_or_group_of_operators:
    """

    class Meta:
        name = "BorderPoint_ValueStructure"

    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_operators_ref_or_group_of_operators: Optional[
        Union[GroupOfOperatorsRef, GroupOfOperators]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperators",
                    "type": GroupOfOperators,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
