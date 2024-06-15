from dataclasses import dataclass

from generated.access_ref_structure import AccessRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRef(AccessRefStructure):
    """
    Reference to an ACCESS link.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
