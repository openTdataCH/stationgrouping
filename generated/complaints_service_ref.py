from dataclasses import dataclass

from generated.complaints_service_ref_structure import (
    ComplaintsServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsServiceRef(ComplaintsServiceRefStructure):
    """
    Identifier of an COMPLAINTS SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
