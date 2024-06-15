from dataclasses import dataclass

from generated.point_on_line_section_versioned_child_structure import (
    PointOnLineSectionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnLineSection(PointOnLineSectionVersionedChildStructure):
    """Inclusion of a POINT on a LINE SECTION.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
