from dataclasses import dataclass

from generated.assistance_service_version_structure import (
    AssistanceServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceService(AssistanceServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE for ASSISTANCE providing information like
    language, accessibility trained staff, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
