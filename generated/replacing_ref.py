from dataclasses import dataclass

from generated.replacing_ref_structure import ReplacingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReplacingRef(ReplacingRefStructure):
    """
    Reference to a REPLACING PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
