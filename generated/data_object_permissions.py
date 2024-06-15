from dataclasses import dataclass, field
from typing import List

from generated.data_object_service_permission_structure import (
    DataObjectServicePermissionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectPermissions:
    """
    Participants permissions to use the service, Only returned if requested.

    :ivar data_object_permission: Permission for a single participant or
        all participants to use an aspect of the service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: List[DataObjectServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectPermission",
            "type": "Element",
        },
    )
