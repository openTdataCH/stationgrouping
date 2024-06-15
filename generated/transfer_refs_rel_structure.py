from dataclasses import dataclass, field
from typing import List, Union

from generated.access_ref import AccessRef
from generated.connection_ref import ConnectionRef
from generated.default_connection_ref import DefaultConnectionRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.site_connection_ref import SiteConnectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a TRANSFER.
    """

    class Meta:
        name = "transferRefs_RelStructure"

    choice: List[
        Union[
            DefaultConnectionRef, SiteConnectionRef, ConnectionRef, AccessRef
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
