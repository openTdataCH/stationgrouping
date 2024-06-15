from dataclasses import dataclass

from generated.service_pattern_version_structure import (
    ServicePatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicePattern(ServicePatternVersionStructure):
    """
    The subset of a JOURNEY PATTERN made up only of STOP POINTs IN JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
