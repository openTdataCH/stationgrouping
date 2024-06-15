from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssignmentVersionStructure2(DataManagedObjectStructure):
    """
    Type for  ASSIGNMENT.

    :ivar name: Name of ASSIGNMENT.
    :ivar description: Description of  ASSIGNMENT.
    :ivar order: Order in which to show  ASSIGNMENT,
    """

    class Meta:
        name = "Assignment_VersionStructure_"

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
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )