from dataclasses import dataclass

from generated.site_facility_set_structure import SiteFacilitySetStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySet(SiteFacilitySetStructure):
    """
    Set of enumerated FACILITY values that are relevant to a SITE (names based on
    TPEG classifications, augmented with UIC etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
