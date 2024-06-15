from dataclasses import dataclass

from generated.journey_layover_structure import JourneyLayoverStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyLayover(JourneyLayoverStructure):
    """Time allowance at the end of each journey on a specified JOURNEY PATTERN, to
    allow for delays and for other purposes.

    This layover supersedes any global layover and may be superseded by
    a specific VEHICLE JOURNEY LAYOVER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
