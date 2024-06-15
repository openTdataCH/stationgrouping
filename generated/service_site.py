from dataclasses import dataclass

from generated.service_site_version_structure import (
    ServiceSiteVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceSite(ServiceSiteVersionStructure):
    """
    A sub-type of SITE which is of specific interest for the operator (e.g. where a
    joint service or a joint fee is proposed).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
