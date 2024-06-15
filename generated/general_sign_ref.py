from dataclasses import dataclass

from generated.general_sign_ref_structure import GeneralSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSignRef(GeneralSignRefStructure):
    """
    Identifier of an GENERAL SIGN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
