from dataclasses import dataclass

from generated.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorRef(OperatorRefStructure):
    """
    Reference to an OPERATOR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
