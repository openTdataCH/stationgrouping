from dataclasses import dataclass

from generated.alternative_name_ref_structure import (
    AlternativeNameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeNameRef(AlternativeNameRefStructure):
    """
    Reference to an ALTERNATIVE NAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
