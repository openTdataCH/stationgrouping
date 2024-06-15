from dataclasses import dataclass

from generated.access_space_version_structure import (
    AccessSpaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpace(AccessSpaceVersionStructure):
    """An area within a STOP PLACE that does not give direct access to transport
    vehicles.

    May be connected to QUAYS by PATH LINKs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
