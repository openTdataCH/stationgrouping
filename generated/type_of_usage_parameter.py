from dataclasses import dataclass

from generated.type_of_usage_parameter_version_structure import (
    TypeOfUsageParameterVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfUsageParameter(TypeOfUsageParameterVersionStructure):
    """
    Category of USAGE PARAMETER user.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
