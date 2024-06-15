from dataclasses import dataclass

from generated.section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParentSectionRef(SectionRefStructure):
    """Reference to a parent SECTION.

    May be omitted if given by context..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
