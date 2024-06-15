from dataclasses import dataclass

from generated.common_section_ref_structure import CommonSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonSectionRef(CommonSectionRefStructure):
    """
    Reference to a COMMON SECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
