from dataclasses import dataclass

from generated.service_link_ref_structure import ServiceLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkRef(ServiceLinkRefStructure):
    """
    Reference to a SERVICE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
