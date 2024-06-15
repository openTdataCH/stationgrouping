from dataclasses import dataclass, field
from typing import Optional

from generated.equipment_version_structure import EquipmentVersionStructure
from generated.type_of_service_feature_refs_rel_structure import (
    TypeOfServiceFeatureRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalServiceVersionStructure(EquipmentVersionStructure):
    """
    Type for a LOCAL SERVICE.

    :ivar types_of_service_feature: Classification of FEATUREs.
    """

    class Meta:
        name = "LocalService_VersionStructure"

    types_of_service_feature: Optional[
        TypeOfServiceFeatureRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "typesOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
