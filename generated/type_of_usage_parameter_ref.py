from dataclasses import dataclass

from generated.type_of_usage_parameter_ref_structure import (
    TypeOfUsageParameterRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfUsageParameterRef(TypeOfUsageParameterRefStructure):
    """
    Reference to a TYPE OF USAGE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
