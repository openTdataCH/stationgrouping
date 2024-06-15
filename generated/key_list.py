from dataclasses import dataclass

from generated.key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class KeyList(KeyListStructure):
    """
    A list of alternative Key values for an element.
    """

    class Meta:
        name = "keyList"
        namespace = "http://www.netex.org.uk/netex"
