from dataclasses import dataclass

from generated.step_limit_ref_structure import StepLimitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StepLimitRef(StepLimitRefStructure):
    """
    Reference to a STEP LIMIT PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
