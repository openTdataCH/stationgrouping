from dataclasses import dataclass

from generated.fare_section_ref_structure import FareSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionRef(FareSectionRefStructure):
    """
    Reference to a FARE SECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
