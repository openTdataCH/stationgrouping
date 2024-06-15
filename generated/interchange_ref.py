from dataclasses import dataclass

from generated.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRef(InterchangeRefStructure):
    """
    Reference to an INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
