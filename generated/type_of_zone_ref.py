from dataclasses import dataclass

from generated.type_of_zone_ref_structure import TypeOfZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfZoneRef(TypeOfZoneRefStructure):
    """
    Reference to a TYPE OF ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
