from dataclasses import dataclass

from generated.service_designator_structure import ServiceDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceDesignator(ServiceDesignatorStructure):
    """Value reference to a SERVICE JOURNEY.

    Provides an alternative way of identifying a Journey between
    SCHEDULED STOP POINTS
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
