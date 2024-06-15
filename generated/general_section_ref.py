from dataclasses import dataclass

from generated.general_section_ref_structure import GeneralSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSectionRef(GeneralSectionRefStructure):
    """
    Reference to a GENERAL SECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
