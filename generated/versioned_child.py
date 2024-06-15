from dataclasses import dataclass

from generated.entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionedChild(VersionedChildStructure):
    """
    A child ENTIITY whose RESPONSIBILITY SET must be the same as its containing
    parent object, and which cannot exist independently of its parent.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
