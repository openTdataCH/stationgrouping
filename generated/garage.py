from dataclasses import dataclass

from generated.garage_version_structure import GarageVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Garage(GarageVersionStructure):
    """A facility used for parking and maintaining vehicles.

    PARKING POINTs in a GARAGE are called GARAGE POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
