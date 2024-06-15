from dataclasses import dataclass

from generated.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReplacingVersionStructure(ResellingVersionStructure):
    """
    Type for REPLACING.
    """

    class Meta:
        name = "Replacing_VersionStructure"
