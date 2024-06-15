from dataclasses import dataclass

from generated.catering_service_ref_structure import (
    CateringServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringServiceRef(CateringServiceRefStructure):
    """
    Identifier of an CATERING SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
