from dataclasses import dataclass

from generated.step_limit_version_structure import StepLimitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StepLimit(StepLimitVersionStructure):
    """
    Geographical parameter limiting the access rights by counts of stops, sections
    or zones.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
