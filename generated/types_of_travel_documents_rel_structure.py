from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_travel_document import TypeOfTravelDocument
from generated.type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfTravelDocumentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF TRAVEL DOCUMENTs.
    """

    class Meta:
        name = "typesOfTravelDocuments_RelStructure"

    type_of_travel_document_ref_or_type_of_travel_document: List[
        Union[TypeOfTravelDocumentRef, TypeOfTravelDocument]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfTravelDocumentRef",
                    "type": TypeOfTravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
