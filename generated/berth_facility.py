from dataclasses import dataclass, field

from generated.berth_facility_enumeration import BerthFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BerthFacility:
    """Classification of BERTHFACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BerthFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
