from dataclasses import dataclass

from generated.blacklist_ref_structure import BlacklistRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistRef(BlacklistRefStructure):
    """
    Reference to a BLACKLIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
