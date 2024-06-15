from dataclasses import dataclass

from generated.type_of_machine_readability_ref_structure import (
    TypeOfMachineReadabilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMachineReadabilityRef(TypeOfMachineReadabilityRefStructure):
    """
    Reference to a TYPE OF MACHINE READABILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
