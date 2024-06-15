from dataclasses import dataclass

from generated.class_of_use_ref_structure import ClassOfUseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassOfUseRef(ClassOfUseRefStructure):
    """
    Reference to a CLASS OF USE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
