from dataclasses import dataclass

from generated.route_instruction_ref_structure import (
    RouteInstructionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstructionRef(RouteInstructionRefStructure):
    """
    Reference to a ROUTE INSTRUCTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
