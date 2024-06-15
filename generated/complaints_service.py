from dataclasses import dataclass

from generated.complaints_service_version_structure import (
    ComplaintsServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsService(ComplaintsServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for COMPLAINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
