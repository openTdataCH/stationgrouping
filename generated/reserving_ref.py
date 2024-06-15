from dataclasses import dataclass

from generated.reserving_ref_structure import ReservingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservingRef(ReservingRefStructure):
    """
    Reference to a RESERVING USAGE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
