from dataclasses import dataclass

from generated.whitelist_version_structure import WhitelistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Whitelist(WhitelistVersionStructure):
    """
    A list of  items (TRAVEL DOCUMENTs, CONTRACTs, etc) explicitly approved for
    processing.+v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
