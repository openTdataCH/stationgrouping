from dataclasses import dataclass

from generated.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PrivateCode(PrivateCodeStructure):
    """A private code that uniquely identifies the element.

    May be used for inter-operating with other (legacy) systems.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
