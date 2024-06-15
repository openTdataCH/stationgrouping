from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.customer import Customer
from generated.customer_ref import CustomerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomersRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMERs.
    """

    class Meta:
        name = "customers_RelStructure"

    customer_ref_or_customer: List[Union[CustomerRef, Customer]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerRef",
                    "type": CustomerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Customer",
                    "type": Customer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
