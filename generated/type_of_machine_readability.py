from dataclasses import dataclass

from generated.type_of_machine_readability_version_structure import (
    TypeOfMachineReadabilityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMachineReadability(TypeOfMachineReadabilityVersionStructure):
    """
    A classification of MACHINE REDABILITY capabailities, used for example to
    indicate how a TRAVEL DOCUMENT may be read.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
