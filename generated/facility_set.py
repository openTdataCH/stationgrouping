from dataclasses import dataclass

from generated.facility_set_version_structure import (
    FacilitySetVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySet(FacilitySetVersionStructure):
    """Facility.

    Set of enumerated FACILITY values (names based on TPEG
    classifications, augmented with UIC etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
