from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfUsageParameterVersionStructure(TypeOfValueVersionStructure):
    """
    Type for TYPE OF USAGE PARAMETER.
    """

    class Meta:
        name = "TypeOfUsageParameter_VersionStructure"
