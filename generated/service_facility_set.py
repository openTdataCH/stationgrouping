from dataclasses import dataclass

from generated.service_facility_set_version_structure import (
    ServiceFacilitySetVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySet(ServiceFacilitySetVersionStructure):
    """Service FACILITY.

    Set of enumerated FACILITY values (Where available names are based
    on TPEG classifications, augmented with UIC etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
