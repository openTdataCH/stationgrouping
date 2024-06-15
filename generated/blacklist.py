from dataclasses import dataclass

from generated.blacklist_version_structure import BlacklistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Blacklist(BlacklistVersionStructure):
    """
    A list of items (TRAVEL DOCUMENTs,  CONTRACTs etc) the validity of which has
    been cancelled temporarily or permanently, for a specific reason like loss of
    the document, technical malfunction, no credit on bank account, offences
    committed by the customer, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
