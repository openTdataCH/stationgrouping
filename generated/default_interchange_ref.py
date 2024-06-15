from dataclasses import dataclass

from generated.default_interchange_ref_structure import (
    DefaultInterchangeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultInterchangeRef(DefaultInterchangeRefStructure):
    """
    Reference to a DEFAULT INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
