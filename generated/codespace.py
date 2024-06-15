from dataclasses import dataclass

from generated.codespace_structure import CodespaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Codespace(CodespaceStructure):
    """A system for uniquely identifying objects of a given type.

    Used for the distributed management of objects from many different
    sources. For example eachregion of a country may be given a
    different codespace to use when allocating stop identifieres which
    will be unique within a country.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
