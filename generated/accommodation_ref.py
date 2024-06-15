from dataclasses import dataclass

from generated.accommodation_ref_structure import AccommodationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationRef(AccommodationRefStructure):
    """
    Reference to a ACCOMMODATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
