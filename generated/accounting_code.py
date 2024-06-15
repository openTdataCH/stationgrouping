from dataclasses import dataclass

from generated.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountingCode(PrivateCodeStructure):
    """
    An Accounting code assigned to the Element (TAP TSI)
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
