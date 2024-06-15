from dataclasses import dataclass

from generated.site_connection_version_structure import (
    SiteConnectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnection(SiteConnectionVersionStructure):
    """
    The physical (spatial) possibility to connect from one point to another in a
    SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
