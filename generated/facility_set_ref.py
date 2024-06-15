from dataclasses import dataclass

from generated.facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySetRef(FacilitySetRefStructure):
    """
    Reference to a FACILITY SET.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
