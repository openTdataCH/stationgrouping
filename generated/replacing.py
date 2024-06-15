from dataclasses import dataclass

from generated.replacing_version_structure import ReplacingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Replacing(ReplacingVersionStructure):
    """
    Whether the product can be replaced if lost or stolen.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
