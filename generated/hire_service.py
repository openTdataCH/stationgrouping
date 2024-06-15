from dataclasses import dataclass

from generated.hire_service_version_structure import (
    HireServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireService(HireServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to hire services (e.g. cycle hire,
    car hire).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
