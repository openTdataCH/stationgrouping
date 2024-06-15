from dataclasses import dataclass

from generated.assistance_service_ref_structure import (
    AssistanceServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceServiceRef(AssistanceServiceRefStructure):
    """
    Identifier of an ASSISTANCE SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
