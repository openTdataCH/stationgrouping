from dataclasses import dataclass

from generated.round_trip_version_structure import RoundTripVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundTrip(RoundTripVersionStructure):
    """
    Properties relating to single or return trip use of a fare.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
