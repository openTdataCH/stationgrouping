from dataclasses import dataclass

from generated.site_facility_set_ref_structure import (
    SiteFacilitySetRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySetRef(SiteFacilitySetRefStructure):
    """
    Reference to a SITE FACILITY SET.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
