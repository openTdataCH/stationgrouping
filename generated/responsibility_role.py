from dataclasses import dataclass

from generated.responsibility_role_version_structure import (
    ResponsibilityRoleVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilityRole(ResponsibilityRoleVersionStructure):
    """A particular role an ORGANISATION or an ORGANISATION PART is playing.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
