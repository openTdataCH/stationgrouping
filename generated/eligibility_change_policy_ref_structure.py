from dataclasses import dataclass

from generated.usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EligibilityChangePolicyRefStructure(UsageParameterRefStructure):
    """
    Type for Reference to an ELIGIBILITY CHANGE POLICY usage parameter.
    """
