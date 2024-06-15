from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingRuleAbstract(DataManagedObjectStructure):
    """
    Dumm abstact type of Pricing rule.
    """

    class Meta:
        name = "PricingRule_"
        namespace = "http://www.netex.org.uk/netex"
