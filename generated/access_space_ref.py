from dataclasses import dataclass

from generated.access_space_ref_structure import AccessSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpaceRef(AccessSpaceRefStructure):
    """
    Reference to an ACCESS SPACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
