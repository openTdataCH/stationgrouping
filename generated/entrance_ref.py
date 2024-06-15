from dataclasses import dataclass

from generated.entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceRef(EntranceRefStructure):
    """
    Reference to an ENTRANCE to a SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
