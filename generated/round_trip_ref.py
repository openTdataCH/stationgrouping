from dataclasses import dataclass

from generated.round_trip_ref_structure import RoundTripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundTripRef(RoundTripRefStructure):
    """
    Reference to a ROUND TRIP PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
