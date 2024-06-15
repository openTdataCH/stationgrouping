from dataclasses import dataclass, field
from typing import List, Union

from generated.day_type_ref import DayTypeRef
from generated.fare_day_type_ref import FareDayTypeRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of DAY TYPEs.
    """

    class Meta:
        name = "dayTypeRefs_RelStructure"

    fare_day_type_ref_or_day_type_ref: List[
        Union[FareDayTypeRef, DayTypeRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
