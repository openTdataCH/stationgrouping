from dataclasses import dataclass

from generated.headway_ref_structure import HeadwayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayRef(HeadwayRefStructure):
    """
    Reference to a HEADWAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
