from dataclasses import dataclass

from generated.interchange_rule_timing_version_structure import (
    InterchangeRuleTimingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleTiming(InterchangeRuleTimingVersionStructure):
    """Conditions for considering journeys to meet or not to meet, specified
    indirectly: by a particular MODE, DIRECTION or LINE.

    Such conditions may alternatively be specified directly, indicating
    the corresponding services. In this case they are either a SERVICE
    JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
