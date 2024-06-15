from dataclasses import dataclass

from generated.minimum_stay_ref_structure import MinimumStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MinimumStayRef(MinimumStayRefStructure):
    """
    Reference to a MINIMUM STAY PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
