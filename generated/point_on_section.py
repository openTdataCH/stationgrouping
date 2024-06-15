from dataclasses import dataclass

from generated.point_on_section_versioned_child_structure import (
    PointOnSectionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnSection(PointOnSectionVersionedChildStructure):
    """POINT  on a SECTION.

    +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
