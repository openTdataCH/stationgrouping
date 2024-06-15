from dataclasses import dataclass

from generated.dated_special_service_version_structure import (
    DatedSpecialServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedSpecialService(DatedSpecialServiceVersionStructure):
    """
    A particular journey of a vehicle on a particular OPERATING DAY including all
    modifications possibly decided by the control staff.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
