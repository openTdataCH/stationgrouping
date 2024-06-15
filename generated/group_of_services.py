from dataclasses import dataclass

from generated.group_of_services_version_structure import (
    GroupOfServicesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServices(GroupOfServicesVersionStructure):
    """
    A group of SERVICEs, often known to its users by a name or a number.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
