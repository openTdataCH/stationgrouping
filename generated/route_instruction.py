from dataclasses import dataclass

from generated.route_instruction_version_structure import (
    RouteInstructionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstruction(RouteInstructionVersionStructure):
    """
    An Instruction on how to follow a ROUTE through the network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
