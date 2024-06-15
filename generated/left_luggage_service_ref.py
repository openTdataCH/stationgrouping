from dataclasses import dataclass

from generated.left_luggage_service_ref_structure import (
    LeftLuggageServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LeftLuggageServiceRef(LeftLuggageServiceRefStructure):
    """
    Identifier of an LEFT LUGGAGE SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
