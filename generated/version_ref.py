from dataclasses import dataclass

from generated.version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionRef(VersionRefStructure):
    """
    Reference to a VERSION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
