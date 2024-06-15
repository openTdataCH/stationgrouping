from dataclasses import dataclass

from generated.ordered_version_of_object_ref_structure import (
    OrderedVersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInSequenceRefStructure(OrderedVersionOfObjectRefStructure):
    """
    Type for a reference to a LINK IN SEQUENCE.
    """
