from dataclasses import dataclass

from generated.coupled_journey_version_structure import (
    CoupledJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoupledJourney(CoupledJourneyVersionStructure):
    """A complete journey operated by a coupled train, composed of two or more
    VEHICLE JOURNEYs remaining coupled together all along a JOURNEY PATTERN.

    A COUPLED JOURNEY may be viewed as a single VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
