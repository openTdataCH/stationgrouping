from dataclasses import dataclass

from generated.lost_property_service_ref_structure import (
    LostPropertyServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyServiceRef(LostPropertyServiceRefStructure):
    """
    Identifier of an LOST PROPERTY SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
