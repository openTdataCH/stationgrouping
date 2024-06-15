from dataclasses import dataclass

from generated.facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetRefStructure(FacilitySetRefStructure):
    """
    Type for a reference to a SERVICE FACILITY SET.
    """
