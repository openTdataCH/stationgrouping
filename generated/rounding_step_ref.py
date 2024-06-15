from dataclasses import dataclass

from generated.rounding_step_ref_structure import RoundingStepRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundingStepRef(RoundingStepRefStructure):
    """
    Reference to a ROUNDING STEP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
