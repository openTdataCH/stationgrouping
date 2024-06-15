from dataclasses import dataclass

from generated.alternative_text_ref_structure import (
    AlternativeTextRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeTextRef(AlternativeTextRefStructure):
    """
    Reference to an ALTERNATIVE TEXT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
