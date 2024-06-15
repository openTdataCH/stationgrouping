from dataclasses import dataclass

from generated.observed_passing_time_ref_structure import (
    ObservedPassingTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimeRef(ObservedPassingTimeRefStructure):
    """
    Reference to an OBSERVED PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
