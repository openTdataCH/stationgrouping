from dataclasses import dataclass

from generated.general_sign_structure import GeneralSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSign(GeneralSignStructure):
    """
    Specialisation of SIGN EQUIPMENT sor signs which are not HEADING SIGNs nor
    PLACE SIGNs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
