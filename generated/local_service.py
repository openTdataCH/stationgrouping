from dataclasses import dataclass

from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalService(LocalServiceVersionStructure):
    """
    A named service relating to the use of the SITE or transport services at a
    particular location, for example porterage, assistance for disabled users,
    booking offices etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
