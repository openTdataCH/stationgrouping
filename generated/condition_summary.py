from dataclasses import dataclass

from generated.condition_summary_structure import ConditionSummaryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConditionSummary(ConditionSummaryStructure):
    """
    Summary description of PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
