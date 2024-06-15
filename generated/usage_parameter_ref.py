from dataclasses import dataclass

from generated.usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterRef(UsageParameterRefStructure):
    """
    Reference to a USAGE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
