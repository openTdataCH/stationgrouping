from dataclasses import dataclass

from generated.service_pattern_ref_structure import ServicePatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicePatternRef(ServicePatternRefStructure):
    """
    Reference to a SERVICE PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
