from dataclasses import dataclass

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDeviceRefStructure(TypeOfValueRefStructure):
    """
    Type for Reference to a TYPE OF RETAIL DEVICE.
    """
