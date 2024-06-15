from dataclasses import dataclass

from generated.retail_consortium_ref_structure import (
    RetailConsortiumRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortiumRef(RetailConsortiumRefStructure):
    """
    Reference to a RETAIL CONSORTIUM.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
