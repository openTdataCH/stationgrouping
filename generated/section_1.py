from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    SectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Section1(SectionVersionStructure):
    """A shared sequence of LINKS or POINTs.

    +v1.1.
    """

    class Meta:
        name = "Section"
        namespace = "http://www.netex.org.uk/netex"
