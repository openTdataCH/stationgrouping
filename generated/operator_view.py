from dataclasses import dataclass

from generated.operator_derived_view_structure import (
    OperatorDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorView(OperatorDerivedViewStructure):
    """Simplified view of OPERATOR.

    All data except the identifier will be derived through the
    relationship.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
