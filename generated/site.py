from dataclasses import dataclass

from generated.site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Site(SiteVersionStructure):
    """
    A type of PLACE, such as a STOP PLACE, POINT OF INTEREST or ADDRESS, to which
    passengers may wish to travel.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
