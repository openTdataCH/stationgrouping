from dataclasses import dataclass

from generated.service_site_ref_structure import ServiceSiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceSiteRef(ServiceSiteRefStructure):
    """
    Reference to a SERVICE SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
