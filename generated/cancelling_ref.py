from dataclasses import dataclass

from generated.cancelling_ref_structure import CancellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CancellingRef(CancellingRefStructure):
    """
    Reference to a CANCELLING PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
