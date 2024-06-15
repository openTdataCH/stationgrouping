from dataclasses import dataclass

from generated.interchanging_ref_structure import InterchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangingRef(InterchangingRefStructure):
    """
    Reference to a INTERCHANGING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
