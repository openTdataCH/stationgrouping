from dataclasses import dataclass

from generated.default_connection_version_structure import (
    DefaultConnectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultConnection(DefaultConnectionVersionStructure):
    """
    Specifies the default transfer times to transfer between MODEs and / or
    OPERATORs within a region.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
