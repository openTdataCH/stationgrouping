from dataclasses import dataclass, field
from typing import Any

from generated.uic_operating_period_version_structure import (
    UicOperatingPeriodVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UicOperatingPeriod(UicOperatingPeriodVersionStructure):
    """
    An OPERATING PERIOD coded in UIC style as a bit string between two dates.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
