from dataclasses import dataclass

from generated.usage_parameter_version_structure import (
    UsageParameterVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameter1(UsageParameterVersionStructure):
    """
    A parameter used to specify the use of a fare system.
    """

    class Meta:
        name = "UsageParameter"
        namespace = "http://www.netex.org.uk/netex"
