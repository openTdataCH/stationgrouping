from dataclasses import dataclass

from generated.observed_passing_time_view_structure import (
    ObservedPassingTimeViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimeView(ObservedPassingTimeViewStructure):
    """
    Simplified OBSERVED PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
