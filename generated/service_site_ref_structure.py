from dataclasses import dataclass

from generated.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceSiteRefStructure(SiteRefStructure):
    """
    Type for identifier of a SERVICE SITE.
    """
