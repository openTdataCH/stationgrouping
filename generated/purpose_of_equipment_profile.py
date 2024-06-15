from dataclasses import dataclass

from generated.purpose_of_equipment_profile_value_structure import (
    PurposeOfEquipmentProfileValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfEquipmentProfile(PurposeOfEquipmentProfileValueStructure):
    """
    A functional purpose which requires a certain set of EQUIPMENT of different
    types put together in a VEHICLE EQUIPMENT PROFILE or STOP POINT EQUIPMENT
    PROFILE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
