from dataclasses import dataclass

from generated.entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallAbstract(VersionedChildStructure):
    """
    Dummy CALL.
    """

    class Meta:
        name = "Call_"
        namespace = "http://www.netex.org.uk/netex"
