from dataclasses import dataclass

from generated.garage_ref_structure import GarageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageRef(GarageRefStructure):
    """
    Reference to a GARAGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
