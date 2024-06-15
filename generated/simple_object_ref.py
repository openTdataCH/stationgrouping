from dataclasses import dataclass

from generated.simple_object_ref_structure import SimpleObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleObjectRef(SimpleObjectRefStructure):
    """
    Simple unversioned reference to a NeTEx ENTITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
