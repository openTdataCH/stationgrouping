from dataclasses import dataclass

from generated.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrameContainmentStructure(RelationshipStructure):
    """
    Type for an implementation of a frame containment relationship  (ENTITY IN
    FRAME IN VERSION) A one to many relationship from the containing parent (one)
    to the contained child (many)
    """

    class Meta:
        name = "frameContainmentStructure"
