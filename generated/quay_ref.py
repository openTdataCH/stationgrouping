from dataclasses import dataclass

from generated.quay_ref_structure import QuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayRef(QuayRefStructure):
    """
    Reference to a QUAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
