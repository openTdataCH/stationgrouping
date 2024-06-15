from dataclasses import dataclass, field
from typing import Optional

from generated.display_assignments_rel_structure import (
    DisplayAssignmentsRelStructure,
)
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogicalDisplayVersionStructure(DataManagedObjectStructure):
    """
    Type for a LOGICAL DISPLAY.

    :ivar name: Name of LOGICAL DISPLAY.
    :ivar description: Description of LOGICAL DISPLAY.
    :ivar display_assignments: DISPLAY ASSIGNMENTs for LOGICAL DISPLAY.
    """

    class Meta:
        name = "LogicalDisplay_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_assignments: Optional[DisplayAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "displayAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
