from dataclasses import dataclass

from generated.type_of_tariff_ref_structure import TypeOfTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTariffRef(TypeOfTariffRefStructure):
    """Reference to a TYPE OF TARIFF.

    (TAP TSI)
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
