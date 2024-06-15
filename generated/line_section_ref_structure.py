from dataclasses import dataclass

from generated.section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionRefStructure(SectionRefStructure):
    """
    Type for a reference to a LINE SECTION.
    """
