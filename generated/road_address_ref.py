from dataclasses import dataclass

from generated.road_address_ref_structure import RoadAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadAddressRef(RoadAddressRefStructure):
    """
    Reference to a Road ADDRESS.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
