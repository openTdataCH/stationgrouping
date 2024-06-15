from dataclasses import dataclass

from generated.facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRef(FacilityRefStructure):
    """
    Reference to a FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
