from dataclasses import dataclass

from generated.retail_service_ref_structure import RetailServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailServiceRef(RetailServiceRefStructure):
    """
    Identifier of an RETAIL SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
