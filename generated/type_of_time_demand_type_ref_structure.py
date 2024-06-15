from dataclasses import dataclass

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTimeDemandTypeRefStructure(TypeOfValueRefStructure):
    """
    Type for a TYPE OF TIME DEMAND TYPE.
    """
