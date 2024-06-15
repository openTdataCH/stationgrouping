from dataclasses import dataclass

from generated.site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceSiteVersionStructure(SiteVersionStructure):
    """
    Type for an identified and data managed element making up a STOP PLACE.
    """

    class Meta:
        name = "ServiceSite_VersionStructure"
