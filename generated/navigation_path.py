from dataclasses import dataclass

from generated.navigation_path_version_structure import (
    NavigationPathVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPath(NavigationPathVersionStructure):
    """A designated path between two places.

    May include an ordered sequence of PATH LINKs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
