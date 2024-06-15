from dataclasses import dataclass, field
from typing import List, Union

from generated.fare_table_ref import FareTableRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to  FARE FARE TABLEs.
    """

    class Meta:
        name = "fareTableRefs_RelStructure"

    standard_fare_table_ref_or_fare_table_ref: List[
        Union[StandardFareTableRef, FareTableRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
