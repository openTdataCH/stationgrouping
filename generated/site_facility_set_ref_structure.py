from dataclasses import dataclass

from generated.facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySetRefStructure(FacilitySetRefStructure):
    """
    Type for a reference to a SITE FACILITY SET.
    """
