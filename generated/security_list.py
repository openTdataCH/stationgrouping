from dataclasses import dataclass

from generated.security_list_version_structure import (
    SecurityListVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityList(SecurityListVersionStructure):
    """
    A list of items whose status is to be accepted or denied for a process such as
    purchase or validation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
