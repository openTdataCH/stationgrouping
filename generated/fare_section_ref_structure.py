from dataclasses import dataclass

from generated.general_section_ref_structure import GeneralSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionRefStructure(GeneralSectionRefStructure):
    """
    Type for Reference to a FARE SECTION.
    """
