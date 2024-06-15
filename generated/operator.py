from dataclasses import dataclass

from generated.operator_version_structure import OperatorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Operator(OperatorVersionStructure):
    """
    A company  providing public transport services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
