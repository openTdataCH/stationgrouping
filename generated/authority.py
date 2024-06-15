from dataclasses import dataclass

from generated.authority_version_structure import AuthorityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Authority(AuthorityVersionStructure):
    """
    The ORGANISATION under which the responsibility of organising the transport
    service in a certain area is placed.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
