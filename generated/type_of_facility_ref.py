from dataclasses import dataclass

from generated.type_of_facility_ref_structure import TypeOfFacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFacilityRef(TypeOfFacilityRefStructure):
    """
    Reference to a TYPE OF FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
