from dataclasses import dataclass

from generated.rounding_step_versioned_child_structure import (
    RoundingStepVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundingStep(RoundingStepVersionedChildStructure):
    """A rounding step to use to round a range of values.

    ANy value larger than the step key and smaller tha the next step key
    should be rounded to this value.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
