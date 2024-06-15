from dataclasses import dataclass

from generated.relationship_ref_structure import RelationshipRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelationshipRef(RelationshipRefStructure):
    """
    Reference to a Relationship.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
