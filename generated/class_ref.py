from dataclasses import dataclass

from generated.class_ref_structure import ClassRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassRef(ClassRefStructure):
    """
    Reference to a Type of an ENTITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
