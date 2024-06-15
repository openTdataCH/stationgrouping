from dataclasses import dataclass, field

from generated.suitable_enumeration import SuitableEnumeration
from generated.user_need_versioned_child_structure import (
    UserNeedVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SuitabilityVersionedChildStructure(UserNeedVersionedChildStructure):
    """
    Type for SUITABILITY.

    :ivar suitable: Whether the facility is suitable.
    """

    class Meta:
        name = "Suitability_VersionedChildStructure"

    suitable: SuitableEnumeration = field(
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
