from dataclasses import dataclass

from generated.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleRefStructure(InterchangeRefStructure):
    """
    Type for a reference to an INTERCHANGE RULE.
    """
